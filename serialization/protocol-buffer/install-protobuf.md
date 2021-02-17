Clone protobuf repo:

    sudo apt-get install autoconf automake libtool curl make g++ unzip -y
    git clone https://github.com/google/protobuf.git
    cd protobuf
    git submodule update --init --recursive

Or download zip of a repo and:

    ./configure
    ./autogen.sh
    make
    make check
    sudo make install
    sudo ldconfig

Check:

    protoc --version

You will need the Python bindings. To install them do:

    pip install protobuf

