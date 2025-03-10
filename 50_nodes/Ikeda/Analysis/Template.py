
import numpy as np
from scipy.signal import fftconvolve

from skimage.util import pad
#from skimage._shared.utils import assert_nD

def assert_nD(array, ndim, arg_name='image'):
    """
    Verify an array meets the desired ndims.
    Parameters
    ----------
    array : array-like
        Input array to be validated
    ndim : int or iterable of ints
        Allowable ndim or ndims for the array.
    arg_name : str, optional
        The name of the array in the original function.
    """
    array = np.asanyarray(array)
    msg = "The parameter `%s` must be a %s-dimensional array"
    if isinstance(ndim, int):
        ndim = [ndim]
    if not array.ndim in ndim:
        raise ValueError(msg % (arg_name, '-or-'.join([str(n) for n in ndim])))

def _window_sum_2d(image, window_shape):

    window_sum = np.cumsum(image, axis=0)
    window_sum = (window_sum[window_shape[0]:-1]
                  - window_sum[:-window_shape[0] - 1])

    window_sum = np.cumsum(window_sum, axis=1)
    window_sum = (window_sum[:, window_shape[1]:-1]
                  - window_sum[:, :-window_shape[1] - 1])

    return window_sum


def _window_sum_3d(image, window_shape):

    window_sum = _window_sum_2d(image, window_shape)

    window_sum = np.cumsum(window_sum, axis=2)
    window_sum = (window_sum[:, :, window_shape[2]:-1]
                  - window_sum[:, :, :-window_shape[2] - 1])

    return window_sum


def match_template(image, template, pad_input=True, mode='constant',
                   constant_values=0):
    """Match a template to a 2-D or 3-D image using normalized correlation.
    The output is an array with values between -1.0 and 1.0. The value at a
    given position corresponds to the correlation coefficient between the image
    and the template.
    For `pad_input=True` matches correspond to the center and otherwise to the
    top-left corner of the template. To find the best match you must search for
    peaks in the response (output) image.
    Parameters
    ----------
    image : (M, N[, D]) array
        2-D or 3-D input image.
    template : (m, n[, d]) array
        Template to locate. It must be `(m <= M, n <= N[, d <= D])`.
    pad_input : bool
        If True, pad `image` so that output is the same size as the image, and
        output values correspond to the template center. Otherwise, the output
        is an array with shape `(M - m + 1, N - n + 1)` for an `(M, N)` image
        and an `(m, n)` template, and matches correspond to origin
        (top-left corner) of the template.
    mode : see `numpy.pad`, optional
        Padding mode.
    constant_values : see `numpy.pad`, optional
        Constant values used in conjunction with ``mode='constant'``.
    Returns
    -------
    output : array
        Response image with correlation coefficients.
    References
    ----------
    .. [1] Briechle and Hanebeck, "Template Matching using Fast Normalized
           Cross Correlation", Proceedings of the SPIE (2001).
    .. [2] J. P. Lewis, "Fast Normalized Cross-Correlation", Industrial Light
           and Magic.
    Examples
    --------
    >>> template = np.zeros((3, 3))
    >>> template[1, 1] = 1
    >>> template
    array([[ 0.,  0.,  0.],
           [ 0.,  1.,  0.],
           [ 0.,  0.,  0.]])
    >>> image = np.zeros((6, 6))
    >>> image[1, 1] = 1
    >>> image[4, 4] = -1
    >>> image
    array([[ 0.,  0.,  0.,  0.,  0.,  0.],
           [ 0.,  1.,  0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  0., -1.,  0.],
           [ 0.,  0.,  0.,  0.,  0.,  0.]])
    >>> result = match_template(image, template)
    >>> np.round(result, 3)
    array([[ 1.   , -0.125,  0.   ,  0.   ],
           [-0.125, -0.125,  0.   ,  0.   ],
           [ 0.   ,  0.   ,  0.125,  0.125],
           [ 0.   ,  0.   ,  0.125, -1.   ]], dtype=float32)
    >>> result = match_template(image, template, pad_input=True)
    >>> np.round(result, 3)
    array([[-0.125, -0.125, -0.125,  0.   ,  0.   ,  0.   ],
           [-0.125,  1.   , -0.125,  0.   ,  0.   ,  0.   ],
           [-0.125, -0.125, -0.125,  0.   ,  0.   ,  0.   ],
           [ 0.   ,  0.   ,  0.   ,  0.125,  0.125,  0.125],
           [ 0.   ,  0.   ,  0.   ,  0.125, -1.   ,  0.125],
           [ 0.   ,  0.   ,  0.   ,  0.125,  0.125,  0.125]], dtype=float32)
    """
    assert_nD(image, (2, 3))

    if image.ndim < template.ndim:
        raise ValueError("Dimensionality of template must be less than or "
                         "equal to the dimensionality of image.")
    if np.any(np.less(image.shape, template.shape)):
        raise ValueError("Image must be larger than template.")

    image_shape = image.shape

    image = np.array(image, dtype=np.float32, copy=False)

    pad_width = tuple((width, width) for width in template.shape)
    if mode == 'constant':
        image = pad(image, pad_width=pad_width, mode=mode,
                    constant_values=constant_values)
    else:
        image = pad(image, pad_width=pad_width, mode=mode)

    # Use special case for 2-D images for much better performance in
    # computation of integral images
    if image.ndim == 2:
        image_window_sum = _window_sum_2d(image, template.shape)
        image_window_sum2 = _window_sum_2d(image ** 2, template.shape)
    elif image.ndim == 3:
        image_window_sum = _window_sum_3d(image, template.shape)
        image_window_sum2 = _window_sum_3d(image ** 2, template.shape)

    template_volume = np.prod(template.shape)
    template_ssd = np.sum((template - template.mean()) ** 2)

    if image.ndim == 2:
        xcorr = fftconvolve(image, template[::-1, ::-1],
                            mode="valid")[1:-1, 1:-1]
    elif image.ndim == 3:
        xcorr = fftconvolve(image, template[::-1, ::-1, ::-1],
                            mode="valid")[1:-1, 1:-1, 1:-1]

    nom = xcorr - image_window_sum * (template.sum() / template_volume)

    denom = image_window_sum2
    np.multiply(image_window_sum, image_window_sum, out=image_window_sum)
    np.divide(image_window_sum, template_volume, out=image_window_sum)
    denom -= image_window_sum
    denom *= template_ssd
    np.maximum(denom, 0, out=denom)  # sqrt of negative number not allowed
    np.sqrt(denom, out=denom)

    response = np.zeros_like(xcorr, dtype=np.float32)

    # avoid zero-division
    mask = denom > np.finfo(np.float32).eps

    response[mask] = nom[mask] / denom[mask]

    slices = []
    for i in range(template.ndim):
        if pad_input:
            d0 = (template.shape[i] - 1) // 2
            d1 = d0 + image_shape[i]
        else:
            d0 = template.shape[i] - 1
            d1 = d0 + image_shape[i] - template.shape[i] + 1
        slices.append(slice(d0, d1))

    return response[slices]
