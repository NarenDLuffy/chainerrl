from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from future import standard_library
from future.utils import with_metaclass
standard_library.install_aliases()

from logging import getLogger

from chainer import cuda
import numpy as np

from chainerrl import explorer


class AdditiveGaussian(explorer.Explorer):
    """Additive Gaussian noise"""

    def __init__(self, scale):
        self.scale = scale

    def select_action(self, t, greedy_action_func):
        a = greedy_action_func()
        noise = np.random.normal(
            scale=self.scale, size=a.shape).astype(np.float32)
        if isinstance(a, cuda.cupy.ndarray):
            noise = cuda.to_gpu(noise)
        return a + noise

    def __repr__(self):
        return 'AdditiveGaussian(scale={})'.format(self.scale)
