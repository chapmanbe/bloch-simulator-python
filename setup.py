from distutils.core import setup, Extension
import numpy

bloch_simulator = Extension("bloch_simulator",
                            include_dirs = [numpy.get_include()],
                            sources = ["bloch/bloch_simulator.c"])
setup(
        name = "Bloch Simulator Library",
        version = "1.0",
        description = "Bloch Simulator and helper modules. Originally written by Brian Hargreaves and Mikki Lustig in Matlab.",
        author = "Niraj Amalkant",
        author_email = "neji49@gmail.com",
        url = "https://github.com/neji49/bloch-simulator-python",
        packages = ["bloch"],
        ext_modules=[bloch_simulator]
        )

