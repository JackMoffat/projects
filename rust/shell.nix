{ pkgs ? import <nixpkgs> {} }:

  pkgs.mkShell rec {
    buildInputs = with pkgs; [
      rustc
      cargo
      llvmPackages_latest.llvm
      llvmPackages_latest.bintools
      zlib.out
      rustup
      xorriso
      grub2
      qemu
      llvmPackages_latest.lld
      python3
    ];
    RUSTC_VERSION = pkgs.lib.readFile ./rust-toolchain;
    # https://github.com/rust-lang/rust-bindgen#environment-variables
    LIBCLANG_PATH= pkgs.lib.makeLibraryPath [ pkgs.llvmPackages_latest.libclang.lib ];
    HISTFILE=toString ./.history;
    # I added the export cargo line below
    # the export PATH should fail. but wait, now I do have a .cargo?
    # for some reason, I now *do* have a ~/.cargo directory. 
    # If I still get no rls, try "export rls=$(which rls)"
    # create a path for the command run by cargo build
    # may need extra variable in the elisp form for rls, but may be fixed by "which rls"
    shellHook = ''
      echo "((nil . ((cargo-process--custom-path-to-bin . \"$(which cargo)\"))))" > .dir-locals.el

      export rls=$(which rls)
      export PATH=$PATH:~/.cargo/bin
      export PATH=$PATH:~/.rustup/toolchains/$RUSTC_VERSION-x86_64-unknown-linux-gnu/bin/
      '';
    # Add libvmi precompiled library to rustc search path
    RUSTFLAGS = (builtins.map (a: ''-L ${a}/lib'') [
      pkgs.libvmi
    ]);
    # Add libvmi, glibc, clang, glib headers to bindgen search path
    BINDGEN_EXTRA_CLANG_ARGS = 
    # Includes with normal include path
    (builtins.map (a: ''-I"${a}/include"'') [
      pkgs.libvmi
      pkgs.glibc.dev 
    ])
    # Includes with special directory paths
    ++ [
      ''-I"${pkgs.llvmPackages_latest.libclang.lib}/lib/clang/${pkgs.llvmPackages_latest.libclang.version}/include"''
      ''-I"${pkgs.glib.dev}/include/glib-2.0"''
      ''-I${pkgs.glib.out}/lib/glib-2.0/include/''
    ];

  }
