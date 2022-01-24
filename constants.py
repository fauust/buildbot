github_status_builders = ["amd64-centos-7", "amd64-debian-10", "amd64-fedora-35", "amd64-ubuntu-2004-clang11", "amd64-windows", "amd64-windows-packages"]

release_builders = ["aarch64-debian-9", "aarch64-debian-9-deb-autobake", "aarch64-debian-11", "aarch64-debian-11-deb-autobake", "aarch64-debian-sid", "aarch64-debian-sid-deb-autobake", "aarch64-fedora-34", "aarch64-fedora-34-rpm-autobake", "aarch64-fedora-35", "aarch64-fedora-35-rpm-autobake", "aarch64-rhel-8", "aarch64-rhel-8-rpm-autobake", "aarch64-ubuntu-2104", "aarch64-ubuntu-2104-deb-autobake", "aarch64-ubuntu-2110", "aarch64-ubuntu-2110-deb-autobake", "amd64-debian-sid", "amd64-debian-sid-deb-autobake", "ppc64le-debian-11", "ppc64le-debian-11-deb-autobake", "ppc64le-debian-sid", "ppc64le-debian-sid-deb-autobake", "s390x-rhel-8"]

builders_quick=["amd64-ubuntu-1804", "amd64-ubuntu-2004", "amd64-ubuntu-2104", "amd64-ubuntu-2110", "amd64-ubuntu-1804-icc", "amd64-ubuntu-2004-fulltest", "amd64-ubuntu-2004-gcc10", "amd64-ubuntu-2004-clang11", "amd64-ubuntu-1804-clang6", "amd64-ubuntu-1804-clang10", "amd64-ubuntu-1804-clang10-asan", "amd64-ubuntu-1804-msan", "x86-ubuntu-1804", "amd64-ubuntu-1804-valgrind", "aarch64-ubuntu-1804", "aarch64-ubuntu-2004", "aarch64-ubuntu-2104", "aarch64-ubuntu-2110", "amd64-rhel-7", "amd64-rhel-8", "amd64-ubuntu-1804-debug", "amd64-debian-9", "x86-debian-9","amd64-debian-10", "amd64-debian-11", "amd64-debian-sid", "x86-debian-sid", "amd64-fedora-34", "amd64-fedora-35", "amd64-centos-7", "amd64-centos-8", "amd64-opensuse-15", "amd64-sles-12", "amd64-sles-15", "ppc64le-debian-9", "ppc64le-debian-10", "ppc64le-debian-11", "ppc64le-debian-sid", "ppc64le-ubuntu-1804", "ppc64le-ubuntu-2004", "ppc64le-ubuntu-2104", "ppc64le-ubuntu-2110", "ppc64le-ubuntu-2004-clang1x", "ppc64le-ubuntu-1804-without-server", "ppc64le-rhel-7", "ppc64le-rhel-8", "ppc64le-centos-7", "aarch64-fedora-35", "aarch64-centos-7", "aarch64-centos-8", "aarch64-debian-10", "aarch64-debian-11", "aarch64-debian-sid", "aarch64-debian-9", "aarch64-rhel-7", "aarch64-rhel-8", "amd64-windows", "amd64-windows-packages", "aix", "x86-debian-9-bintar-systemd", "x86-debian-9-bintar-initd", "amd64-debian-9-bintar-systemd", "amd64-debian-9-bintar-initd", "aarch64-centos-7-bintar-systemd", "aarch64-centos-7-bintar-initd", "ppc64le-debian-9-bintar-systemd", "ppc64le-debian-9-bintar-initd", "s390x-ubuntu-2004", "s390x-rhel-8", "s390x-sles-15"]
builders_quick = list(filter(lambda x: x not in github_status_builders, builders_quick))

builders_autobake=["amd64-centos-7-rpm-autobake", "amd64-centos-8-rpm-autobake", "amd64-debian-9-deb-autobake", "x86-debian-9-deb-autobake", "amd64-debian-10-deb-autobake", "amd64-debian-11-deb-autobake", "amd64-debian-sid-deb-autobake", "x86-debian-sid-deb-autobake", "amd64-fedora-34-rpm-autobake", "amd64-fedora-35-rpm-autobake", "amd64-rhel-7-rpm-autobake", "amd64-rhel-8-rpm-autobake", "amd64-opensuse-15-rpm-autobake", "amd64-sles-12-rpm-autobake", "amd64-sles-15-rpm-autobake", "amd64-ubuntu-1804-deb-autobake", "amd64-ubuntu-2004-deb-autobake", "amd64-ubuntu-2104-deb-autobake", "amd64-ubuntu-2110-deb-autobake", "aarch64-ubuntu-1804-deb-autobake", "aarch64-ubuntu-2004-deb-autobake", "aarch64-ubuntu-2104-deb-autobake", "aarch64-ubuntu-2110-deb-autobake", "ppc64le-debian-9-deb-autobake", "ppc64le-debian-10-deb-autobake", "ppc64le-debian-11-deb-autobake", "ppc64le-debian-sid-deb-autobake", "ppc64le-ubuntu-1804-deb-autobake", "ppc64le-ubuntu-2004-deb-autobake", "ppc64le-ubuntu-2104-deb-autobake", "ppc64le-ubuntu-2110-deb-autobake", "ppc64le-centos-7-rpm-autobake", "ppc64le-rhel-7-rpm-autobake", "ppc64le-rhel-8-rpm-autobake", "aarch64-debian-10-deb-autobake", "aarch64-debian-11-deb-autobake", "aarch64-debian-sid-deb-autobake", "aarch64-debian-9-deb-autobake", "aarch64-fedora-34-rpm-autobake", "aarch64-fedora-35-rpm-autobake", "aarch64-centos-7-rpm-autobake", "aarch64-centos-8-rpm-autobake", "aarch64-rhel-7-rpm-autobake", "aarch64-rhel-8-rpm-autobake", "s390x-ubuntu-2004-deb-autobake", "s390x-rhel-8-rpm-autobake", "s390x-sles-15-rpm-autobake"]

builders_big=["amd64-ubuntu-1804-bigtest"]

builders_install=["amd64-ubuntu-1804-deb-autobake-install", "amd64-centos-7-rpm-autobake-install"]

builders_upgrade=["amd64-ubuntu-1804-deb-autobake-major-upgrade", "amd64-ubuntu-1804-deb-autobake-minor-upgrade", "amd64-centos-7-rpm-autobake-major-upgrade", "amd64-centos-7-rpm-autobake-minor-upgrade"]

builders_eco=["amd64-ubuntu-2004-eco-php", "amd64-debian-10-eco-pymysql", "amd64-debian-10-eco-mysqljs", "amd64-ubuntu-2004-eco-dbdeployer"]

builders_dockerlibrary=["amd64-rhel8-dockerlibrary"]

supportedPlatforms = {}
supportedPlatforms["10.2"] = ['aarch64-centos-7', 'aarch64-centos-8', 'aarch64-debian-10', 'aarch64-debian-9', 'aarch64-rhel-7', 'aarch64-rhel-8', 'aarch64-ubuntu-1804', 'amd64-centos-7', 'amd64-debian-10', 'amd64-debian-9', 'amd64-opensuse-15', 'amd64-rhel-7', 'amd64-rhel-8', 'amd64-sles-12', 'amd64-sles-15', 'amd64-ubuntu-1804', 'amd64-ubuntu-1804-clang10', 'amd64-ubuntu-1804-clang10-asan', 'amd64-ubuntu-1804-clang6', 'amd64-ubuntu-1804-valgrind', 'amd64-ubuntu-2004', 'amd64-ubuntu-2004-clang11', 'amd64-windows', 'amd64-windows-packages', 'ppc64le-centos-7', 'ppc64le-debian-9', 'ppc64le-rhel-7', 'ppc64le-rhel-8', 'ppc64le-ubuntu-1804', 'x86-debian-9', 'x86-ubuntu-1804']
supportedPlatforms["10.3"] = ['aarch64-centos-7', 'aarch64-centos-8', 'aarch64-debian-10', 'aarch64-debian-9', 'aarch64-rhel-7', 'aarch64-rhel-8', 'aarch64-ubuntu-1804', 'aarch64-ubuntu-2004', 'amd64-centos-7', 'amd64-centos-8', 'amd64-debian-10', 'amd64-debian-9', 'amd64-opensuse-15', 'amd64-rhel-7', 'amd64-rhel-8', 'amd64-sles-12', 'amd64-sles-15', 'amd64-ubuntu-1804', 'amd64-ubuntu-1804-clang10', 'amd64-ubuntu-1804-clang10-asan', 'amd64-ubuntu-1804-clang6', 'amd64-ubuntu-1804-debug', 'amd64-ubuntu-1804-valgrind', 'amd64-ubuntu-2004', 'amd64-ubuntu-2004-clang11', 'amd64-windows', 'amd64-windows-packages', 'ppc64le-centos-7', 'ppc64le-centos-8', 'ppc64le-debian-10', 'ppc64le-debian-9', 'ppc64le-rhel-7', 'ppc64le-rhel-8', 'ppc64le-ubuntu-1804', 'ppc64le-ubuntu-2004-clang1x', 'ppc64le-ubuntu-1804-without-server', 'ppc64le-ubuntu-2004', 'x86-debian-9', 'x86-debian-9-bintar-systemd', 'x86-debian-9-bintar-initd', 'amd64-debian-9-bintar-systemd', 'amd64-debian-9-bintar-initd', 'aarch64-centos-7-bintar-systemd', 'aarch64-centos-7-bintar-initd', 'ppc64le-debian-9-bintar-systemd', 'ppc64le-debian-9-bintar-initd']
supportedPlatforms["10.4"] = ['aarch64-centos-7', 'aarch64-centos-8', 'aarch64-debian-10', 'aarch64-debian-9', 'aarch64-rhel-7', 'aarch64-rhel-8', 'aarch64-ubuntu-1804', 'aarch64-ubuntu-2004', 'amd64-centos-7', 'amd64-centos-8', 'amd64-debian-10', 'amd64-debian-9', 'amd64-opensuse-15', 'amd64-rhel-7', 'amd64-rhel-8', 'amd64-sles-12', 'amd64-sles-15', 'amd64-ubuntu-1804', 'amd64-ubuntu-1804-clang10', 'amd64-ubuntu-1804-clang10-asan', 'amd64-ubuntu-1804-clang6', 'amd64-ubuntu-1804-debug', 'amd64-ubuntu-1804-valgrind', 'amd64-ubuntu-2004', 'amd64-ubuntu-2004-clang11', 'amd64-windows', 'amd64-windows-packages', 'ppc64le-centos-7', 'ppc64le-centos-8', 'ppc64le-debian-10', 'ppc64le-debian-9', 'ppc64le-rhel-7', 'ppc64le-rhel-8', 'ppc64le-ubuntu-1804', 'ppc64le-ubuntu-2004-clang1x', 'ppc64le-ubuntu-1804-without-server', 'ppc64le-ubuntu-2004', 'x86-debian-9', 'x86-debian-9-bintar-systemd', 'x86-debian-9-bintar-initd', 'amd64-debian-9-bintar-systemd', 'amd64-debian-9-bintar-initd', 'aarch64-centos-7-bintar-systemd', 'aarch64-centos-7-bintar-initd', 'ppc64le-debian-9-bintar-systemd', 'ppc64le-debian-9-bintar-initd']
supportedPlatforms["10.5"] = ['aarch64-centos-7', 'aarch64-centos-8', 'aarch64-debian-10', 'aarch64-debian-11', 'aarch64-debian-9', 'aarch64-debian-sid', 'aarch64-fedora-34', "aarch64-fedora-35", 'aarch64-rhel-7', 'aarch64-rhel-8', 'aarch64-ubuntu-1804', 'aarch64-ubuntu-2004', 'aarch64-ubuntu-2104', "aarch64-ubuntu-2110", 'amd64-centos-7', 'amd64-centos-8', 'amd64-debian-10', 'amd64-debian-11', 'amd64-debian-9', 'amd64-debian-sid', 'amd64-fedora-34', 'amd64-fedora-35', 'amd64-opensuse-15', 'amd64-rhel-7', 'amd64-rhel-8', 'amd64-sles-12', 'amd64-sles-15', 'amd64-ubuntu-1804', 'amd64-ubuntu-1804-clang10', 'amd64-ubuntu-1804-clang10-asan', 'amd64-ubuntu-1804-clang6', 'amd64-ubuntu-1804-debug', 'amd64-ubuntu-1804-msan', 'amd64-ubuntu-1804-valgrind', 'amd64-ubuntu-2004', 'amd64-ubuntu-2004-clang11', 'amd64-ubuntu-2004-fulltest', 'amd64-ubuntu-2004-gcc10', 'amd64-ubuntu-1804-icc', 'amd64-ubuntu-2104', 'amd64-ubuntu-2110', 'amd64-windows', 'amd64-windows-packages', 'ppc64le-centos-7', 'ppc64le-debian-10', 'ppc64le-debian-11', 'ppc64le-debian-9', 'ppc64le-debian-sid', 'ppc64le-rhel-7', 'ppc64le-rhel-8', 'ppc64le-ubuntu-1804', 'ppc64le-ubuntu-2004-clang1x', 'ppc64le-ubuntu-1804-without-server', 'ppc64le-ubuntu-2004', 'ppc64le-ubuntu-2104', 'ppc64le-ubuntu-2110', 'x86-debian-9', 'x86-debian-sid', 'x86-ubuntu-1804', 'x86-debian-9-bintar-systemd', 'x86-debian-9-bintar-initd', 'amd64-debian-9-bintar-systemd', 'amd64-debian-9-bintar-initd', 'aarch64-centos-7-bintar-systemd', 'aarch64-centos-7-bintar-initd', 'ppc64le-debian-9-bintar-systemd', 'ppc64le-debian-9-bintar-initd', 'aix', 's390x-ubuntu-2004', 's390x-rhel-8', 's390x-sles-15']
supportedPlatforms["10.6"] = ['aarch64-centos-7', 'aarch64-centos-8', 'aarch64-debian-10', 'aarch64-debian-11', 'aarch64-debian-9', 'aarch64-debian-sid', 'aarch64-fedora-34', "aarch64-fedora-35", 'aarch64-rhel-7', 'aarch64-rhel-8', 'aarch64-ubuntu-1804', 'aarch64-ubuntu-2004', 'aarch64-ubuntu-2104', "aarch64-ubuntu-2110", 'amd64-centos-7', 'amd64-centos-8', 'amd64-debian-10', 'amd64-debian-11', 'amd64-debian-9', 'amd64-debian-sid', 'amd64-fedora-34', 'amd64-fedora-35', 'amd64-opensuse-15', 'amd64-rhel-7', 'amd64-rhel-8', 'amd64-sles-12', 'amd64-sles-15', 'amd64-ubuntu-1804', 'amd64-ubuntu-1804-clang10', 'amd64-ubuntu-1804-clang10-asan', 'amd64-ubuntu-1804-clang6', 'amd64-ubuntu-1804-debug', 'amd64-ubuntu-1804-msan', 'amd64-ubuntu-1804-valgrind', 'amd64-ubuntu-2004', 'amd64-ubuntu-2004-clang11', 'amd64-ubuntu-2004-fulltest', 'amd64-ubuntu-2004-gcc10', 'amd64-ubuntu-1804-icc', 'amd64-ubuntu-2104', 'amd64-ubuntu-2110', 'amd64-windows', 'amd64-windows-packages', 'ppc64le-centos-7', 'ppc64le-debian-10', 'ppc64le-debian-11', 'ppc64le-debian-9', 'ppc64le-debian-sid', 'ppc64le-rhel-7', 'ppc64le-rhel-8', 'ppc64le-ubuntu-1804', 'ppc64le-ubuntu-2004-clang1x', 'ppc64le-ubuntu-1804-without-server', 'ppc64le-ubuntu-2004', 'ppc64le-ubuntu-2104', 'ppc64le-ubuntu-2110', 'x86-debian-9', 'x86-debian-sid', 'x86-ubuntu-1804', 'x86-debian-9-bintar-systemd', 'x86-debian-9-bintar-initd', 'amd64-debian-9-bintar-systemd', 'amd64-debian-9-bintar-initd', 'aarch64-centos-7-bintar-systemd', 'aarch64-centos-7-bintar-initd', 'ppc64le-debian-9-bintar-systemd', 'ppc64le-debian-9-bintar-initd', 'aix', 's390x-ubuntu-2004', 's390x-rhel-8', 's390x-sles-15']
supportedPlatforms["10.7"] = ['aarch64-centos-7', 'aarch64-centos-8', 'aarch64-debian-10', 'aarch64-debian-11', 'aarch64-debian-9', 'aarch64-debian-sid', 'aarch64-fedora-34', "aarch64-fedora-35", 'aarch64-rhel-7', 'aarch64-rhel-8', 'aarch64-ubuntu-1804', 'aarch64-ubuntu-2004', 'aarch64-ubuntu-2104', "aarch64-ubuntu-2110", 'amd64-centos-7', 'amd64-centos-8', 'amd64-debian-10', 'amd64-debian-11', 'amd64-debian-9', 'amd64-debian-sid', 'amd64-fedora-34', 'amd64-fedora-35', 'amd64-opensuse-15', 'amd64-rhel-7', 'amd64-rhel-8', 'amd64-sles-12', 'amd64-sles-15', 'amd64-ubuntu-1804', 'amd64-ubuntu-1804-clang10', 'amd64-ubuntu-1804-clang10-asan', 'amd64-ubuntu-1804-clang6', 'amd64-ubuntu-1804-debug', 'amd64-ubuntu-1804-msan', 'amd64-ubuntu-1804-valgrind', 'amd64-ubuntu-2004', 'amd64-ubuntu-2004-clang11', 'amd64-ubuntu-2004-fulltest', 'amd64-ubuntu-2004-gcc10', 'amd64-ubuntu-1804-icc', 'amd64-ubuntu-2104', 'amd64-ubuntu-2110', 'amd64-windows', 'amd64-windows-packages', 'ppc64le-centos-7', 'ppc64le-debian-10', 'ppc64le-debian-11', 'ppc64le-debian-9', 'ppc64le-debian-sid', 'ppc64le-rhel-7', 'ppc64le-rhel-8', 'ppc64le-ubuntu-1804', 'ppc64le-ubuntu-2004-clang1x', 'ppc64le-ubuntu-1804-without-server', 'ppc64le-ubuntu-2004', 'ppc64le-ubuntu-2104', 'ppc64le-ubuntu-2110', 'x86-debian-9', 'x86-debian-sid', 'x86-ubuntu-1804', 'x86-debian-9-bintar-systemd', 'x86-debian-9-bintar-initd', 'amd64-debian-9-bintar-systemd', 'amd64-debian-9-bintar-initd', 'aarch64-centos-7-bintar-systemd', 'aarch64-centos-7-bintar-initd', 'ppc64le-debian-9-bintar-systemd', 'ppc64le-debian-9-bintar-initd', 'aix', 's390x-ubuntu-2004', 's390x-rhel-8', 's390x-sles-15']
supportedPlatforms["10.8"] = ['aarch64-centos-7', 'aarch64-centos-8', 'aarch64-debian-10', 'aarch64-debian-11', 'aarch64-debian-9', 'aarch64-debian-sid', 'aarch64-fedora-34', "aarch64-fedora-35", 'aarch64-rhel-7', 'aarch64-rhel-8', 'aarch64-ubuntu-1804', 'aarch64-ubuntu-2004', 'aarch64-ubuntu-2104', "aarch64-ubuntu-2110", 'amd64-centos-7', 'amd64-centos-8', 'amd64-debian-10', 'amd64-debian-11', 'amd64-debian-9', 'amd64-debian-sid', 'amd64-fedora-34', 'amd64-fedora-35', 'amd64-opensuse-15', 'amd64-rhel-7', 'amd64-rhel-8', 'amd64-sles-12', 'amd64-sles-15', 'amd64-ubuntu-1804', 'amd64-ubuntu-1804-clang10', 'amd64-ubuntu-1804-clang10-asan', 'amd64-ubuntu-1804-clang6', 'amd64-ubuntu-1804-debug', 'amd64-ubuntu-1804-msan', 'amd64-ubuntu-1804-valgrind', 'amd64-ubuntu-2004', 'amd64-ubuntu-2004-clang11', 'amd64-ubuntu-2004-fulltest', 'amd64-ubuntu-2004-gcc10', 'amd64-ubuntu-1804-icc', 'amd64-ubuntu-2104', 'amd64-ubuntu-2110', 'amd64-windows', 'amd64-windows-packages', 'ppc64le-centos-7', 'ppc64le-debian-10', 'ppc64le-debian-11', 'ppc64le-debian-9', 'ppc64le-debian-sid', 'ppc64le-rhel-7', 'ppc64le-rhel-8', 'ppc64le-ubuntu-1804', 'ppc64le-ubuntu-2004-clang1x', 'ppc64le-ubuntu-1804-without-server', 'ppc64le-ubuntu-2004', 'ppc64le-ubuntu-2104', 'ppc64le-ubuntu-2110', 'x86-debian-9', 'x86-debian-sid', 'x86-ubuntu-1804', 'x86-debian-9-bintar-systemd', 'x86-debian-9-bintar-initd', 'amd64-debian-9-bintar-systemd', 'amd64-debian-9-bintar-initd', 'aarch64-centos-7-bintar-systemd', 'aarch64-centos-7-bintar-initd', 'ppc64le-debian-9-bintar-systemd', 'ppc64le-debian-9-bintar-initd', 'aix', 's390x-ubuntu-2004', 's390x-rhel-8', 's390x-sles-15']

# Hack to remove all github_status_builders since they are triggered separately
for k in supportedPlatforms:
    supportedPlatforms[k] = list(filter(lambda x: x not in github_status_builders, supportedPlatforms[k]))

