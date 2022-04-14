{ nixpkgs ? import <nixpkgs> {} }:
# getting help from https://gutier.io/post/development-using-rust-with-nix/
let
  rustOverlay = builtins.fetchTarball "https://github.com/oxalica/rust-overlay/archive/master.tar.gz";
  pinnedPkgs = nixpkgs.fetchFromGitHub {
    owner  = "NixOS";
    repo   = "nixpkgs";
    rev    = "1fe6ed37fd9beb92afe90671c0c2a662a03463dd";
    sha256 = "1daa0y3p17shn9gibr321vx8vija6bfsb5zd7h4pxdbbwjkfq8n2";
  };
  pkgs = import pinnedPkgs {
    overlays = [ (import rustOverlay) ];
  };
in
  pkgs.mkShell rec {
    buildInputs = with pkgs; [
      llvmPackages_latest.llvm
      llvmPackages_latest.bintools
      llvmPackages_latest.lld
      rust-bin.stable.latest.default
      rust-analyzer
      xorg.libX11
      python3
      #wgpu-utils
      #rustc
      #rustup
      # cargo
      llvmPackages_latest.bintools
      #zlib.out
      #xorriso
      #grub2
      llvmPackages_latest.lld
    ];
    #RUSTC_VERSION = pkgs.lib.readFile ./rust-toolchain;
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
      #export rls=$(which rls)
      #export PATH=$PATH:~/.cargo/bin
      #export PATH=$PATH:~/.rustup/toolchains/$RUSTC_VERSION-x86_64-unknown-linux-gnu/bin/
      '';
  }
