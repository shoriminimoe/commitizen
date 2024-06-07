import subprocess

from commitizen.providers.base_provider import VersionProvider


class HatchProvider(VersionProvider):
    def get_version(self) -> str:
        return (
            subprocess.run(["hatch", "version"], stdout=subprocess.PIPE)
            .stdout.decode()
            .strip()
        )

    def set_version(self, version: str) -> None:
        subprocess.run(["hatch", "version", version])
