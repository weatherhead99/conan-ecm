from conans import ConanFile, CMake

class TestPackageConan(ConanFile):
    generators = "cmake"

    def test(self):
        cmake = CMake(self)
        cmake.configure()
        
