import os
import sys
from pathlib import Path
from types import ModuleType
# mypy: disable-error-code="name-defined"

# __all__ is computed below.
__pre_all__ = ["QtCore", "QtGui", "QtWidgets", "QtPrintSupport", "QtSql", "QtNetwork", "QtTest", "QtConcurrent", "QtDBus", "QtDesigner", "QtXml", "QtHelp", "QtMultimedia", "QtMultimediaWidgets", "QtOpenGL", "QtOpenGLWidgets", "QtPdf", "QtPdfWidgets", "QtPositioning", "QtLocation", "QtNetworkAuth", "QtNfc", "QtQml", "QtQuick", "QtQuick3D", "QtQuickControls2", "QtQuickTest", "QtQuickWidgets", "QtRemoteObjects", "QtScxml", "QtSensors", "QtSerialPort", "QtSerialBus", "QtStateMachine", "QtTextToSpeech", "QtCharts", "QtSpatialAudio", "QtSvg", "QtSvgWidgets", "QtDataVisualization", "QtGraphs", "QtGraphsWidgets", "QtBluetooth", "QtUiTools", "QtAxContainer", "QtWebChannel", "QtWebEngineCore", "QtWebEngineWidgets", "QtWebEngineQuick", "QtWebSockets", "QtHttpServer", "QtWebView", "Qt3DCore", "Qt3DRender", "Qt3DInput", "Qt3DLogic", "Qt3DAnimation", "Qt3DExtras"]
__version__ = "6.8.2.1"
__version_info__ = (6, 8, 2.1, "", "")

SKIP_MYPY_TEST = bool("")


def _additional_dll_directories(package_dir):
    # Find shiboken6 relative to the package directory.
    root = Path(package_dir).parent
    # Check for a flat .zip as deployed by cx_free(PYSIDE-1257)
    if root.suffix == '.zip':
        return []
    shiboken6 = root / 'shiboken6'
    if shiboken6.is_dir():  # Standard case, only shiboken6 is needed
        return [shiboken6]
    # The below code is for the build process when generate_pyi.py
    # is executed in the build directory. We need libpyside and Qt in addition.
    shiboken6 = Path(root).parent / 'shiboken6' / 'libshiboken'
    if not shiboken6.is_dir():
        raise ImportError(str(shiboken6) + ' does not exist')
    result = [shiboken6, root / 'libpyside']
    libpysideqml = root / 'libpysideqml'
    if libpysideqml.is_dir():
        result.append(libpysideqml)
    for path in os.environ.get('PATH').split(';'):
        if path:
            if (Path(path) / 'qmake.exe').exists():
                result.append(path)
                break
    return result


def _setupQtDirectories():
    # On Windows we need to explicitly import the shiboken6 module so
    # that the libshiboken.dll dependency is loaded by the time a
    # Qt module is imported. Otherwise due to PATH not containing
    # the shiboken6 module path, the Qt module import would fail
    # due to the missing libshiboken dll.
    # In addition, as of Python 3.8, the shiboken package directory
    # must be added to the DLL search paths so that shiboken6.dll
    # is found.
    # We need to do the same on Linux and macOS, because we do not
    # embed rpaths into the PySide6 libraries that would point to
    # the libshiboken library location. Importing the module
    # loads the libraries into the process memory beforehand, and
    # thus takes care of it for us.

    pyside_package_dir = Path(__file__).parent.resolve()

    if sys.platform == 'win32':
        for dir in _additional_dll_directories(pyside_package_dir):
            os.add_dll_directory(os.fspath(dir))

    try:
        # PYSIDE-1497: we use the build dir or install dir or site-packages, whatever the path
        #              setting dictates. There is no longer a difference in path structure.
        global Shiboken
        from shiboken6 import Shiboken
    except Exception:
        paths = ', '.join(sys.path)
        print(f"PySide6/__init__.py: Unable to import Shiboken from {paths}",
              file=sys.stderr)
        raise

    if sys.platform == 'win32':
        # PATH has to contain the package directory, otherwise plugins
        # won't be able to find their required Qt libraries (e.g. the
        # svg image plugin won't find Qt5Svg.dll).
        os.environ['PATH'] = os.fspath(pyside_package_dir) + os.pathsep + os.environ['PATH']

        # On Windows, add the PySide6\openssl folder (created by setup.py's
        # --openssl option) to the PATH so that the SSL DLLs can be found
        # when Qt tries to dynamically load them. Tell Qt to load them and
        # then reset the PATH.
        openssl_dir = pyside_package_dir / 'openssl'
        if openssl_dir.exists():
            path = os.environ['PATH']
            try:
                os.environ['PATH'] = os.fspath(openssl_dir) + os.pathsep + path
                try:
                    from . import QtNetwork
                except ImportError:
                    pass
                else:
                    QtNetwork.QSslSocket.supportsSsl()
            finally:
                os.environ['PATH'] = path


def _find_all_qt_modules():
    # Since the wheel split, the __all__ variable cannot be computed statically,
    # because we don't know all modules in advance.

    # Instead, we use __getattr__ which is supported since Python 3.7
    # and create the __all__ list on demand when needed.
    location = Path(__file__).resolve().parent
    files = os.listdir(location)
    unordered = set(name[: name.find(".")] for name in files if name.startswith("Qt") and (
                                                                name.endswith((".pyd", ".so"))))
    ordered_part = __pre_all__
    result = []
    for name in ordered_part:
        if name in unordered:
            result.append(name)
            unordered.remove(name)
    result.extend(unordered)
    return result


# Provide the __all__ variable only on access.
def __getattr__(name: str) -> list[str]:
    if name == "__all__":
        global __all__
        __all__ = _find_all_qt_modules()
        return __all__
    raise AttributeError(f"module '{__name__}' has no attribute '{name}' :)")


# Be prepared that people can access the module dict instead.
class ModuleDict(dict):
    def __missing__(self, key):
        if key == "__all__":
            self[key] = __all__ if "__all__" in globals() else __getattr__("__all__")
            return __all__
        raise KeyError(f"dict of module '{__name__}' has no key '{key}' :)")


class SubModule(ModuleType):
    pass


_setupQtDirectories()
Shiboken.replaceModuleDict(sys.modules["PySide6"], SubModule, ModuleDict(globals()))
