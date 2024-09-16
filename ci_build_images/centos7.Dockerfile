# Buildbot worker for building MariaDB
#
# Provides a base CentOS image with latest buildbot worker installed
# and MariaDB build dependencies

ARG BASE_IMAGE
FROM "$BASE_IMAGE"
LABEL maintainer="MariaDB Buildbot maintainers"

# Install updates and required packages
RUN sed -i -e 's/mirrorlist/#mirrorlist/g' \
           -e 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-* \
    && yum -y --enablerepo=extras install epel-release \
    && sed -i -e '/baseurl/s/^#//g' \
              -e  's:download.fedoraproject.org/pub:dl.fedoraproject.org/pub/archive/:' \
              -e '/metalink/s/^/#/g' /etc/yum.repos.d/epel.repo \
    && yum -y upgrade \
    && yum -y groupinstall 'Development Tools' \
    && yum-builddep -y mariadb-server \
    && yum -y install \
    Judy-devel \
    boost-devel \
    bzip2 \
    bzip2-devel \
    ccache \
    check-devel \
    cmake3 \
    cracklib-devel \
    createrepo \
    curl-devel \
    galera \
    gnutls-devel \
    java-1.8.0-openjdk-devel \
    java-1.8.0-openjdk \
    jemalloc-devel \
    libcurl-devel \
    libevent-devel \
    libffi-devel \
    libxml2-devel \
    libzstd-devel \
    lz4-devel \
    pcre2-devel \
    perl-autodie \
    perl-Net-SSLeay \
    python3 \
    python3-pip \
    rpmlint \
    ruby \
    snappy-devel \
    systemd-devel \
    unixODBC \
    unixODBC-devel \
    wget \
    which \
    xz-devel \
    && yum clean all \
    && alternatives --install /usr/local/bin/cmake cmake /usr/bin/cmake3 20 \
    --slave /usr/local/bin/ctest ctest /usr/bin/ctest3 \
    --slave /usr/local/bin/cpack cpack /usr/bin/cpack3 \
    --slave /usr/local/bin/ccmake ccmake /usr/bin/ccmake3 \
    --family cmake \
    # dumb-init rpm is not available on centos
    && curl -sL "https://github.com/Yelp/dumb-init/releases/download/v1.2.5/dumb-init_1.2.5_$(uname -m)" >/usr/local/bin/dumb-init \
    && chmod +x /usr/local/bin/dumb-init

ENV WSREP_PROVIDER=/usr/lib64/galera/libgalera_smm.so
