import os
from conans import ConanFile, CMake, tools

class ECMConan(ConanFile):
    name = "extra-cmake-modules"
    version = "5.50.0"
    url = "https://github.com/KDE/extra-cmake-modules"
    description = "Extra modules and scripts for CMake."
    generators="cmake"
    sha256="edf6f7895c307afae893200c759f8bb4803650f61b39409f3fce6a9efd50746d"
    #build_requires="Qt/5.11.0@bincrafters/stable"
    short_paths=True

    def source(self):
        tools.get("https://github.com/KDE/extra-cmake-modules/archive/v%s.tar.gz"
                  % self.version, sha256=self.sha256)

    def build(self):
        cmake = CMake(self)
        sf = os.path.join(self.source_folder,"extra-cmake-modules-%s" % self.version)
        cmake.definitions["BUILD_TESTING"] = "OFF"
        cmake.definitions["BUILD_HTML_DOCS"] = "OFF"
        cmake.definitions["BUILD_MAN_DOCS"] = "OFF"
        cmake.definitions["BUILD_QTHELP_DOCS"] = "OFF"
        
        cmake.configure(source_folder=sf)
        cmake.build()
        cmake.install()

    def package(self):
        pass

    
