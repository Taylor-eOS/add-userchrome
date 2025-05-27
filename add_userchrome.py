import os,argparse,textwrap

CSS_BLOCK = textwrap.dedent("""\
navigator-toolbox { border-bottom: none !important; }
nav-bar,
identity-box,
tabbrowser-tabs,
TabsToolbar,
nav-bar * { visibility: collapse !important; }
#TabsToolbar {
  display: none !important;
}
""")

def process(path,apply):
    chrome_dir=os.path.join(path,"chrome")
    target=os.path.join(chrome_dir,"userChrome.css")
    os.makedirs(chrome_dir,exist_ok=True)
    if os.path.exists(target):
        with open(target,"r",encoding="utf-8") as f:
            content=f.read()
    else:
        content=""
    if "display: none !important;" in content:
        print(f"{os.path.basename(path)}: already up to date")
    else:
        print(f"{os.path.basename(path)}: will append CSS" if not apply else f"{os.path.basename(path)}: appending CSS")
        if apply:
            with open(target,"a",encoding="utf-8") as f:
                if content and not content.endswith("\n"):
                    f.write("\n")
                f.write(CSS_BLOCK)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--apply",action="store_true",help="actually write changes")
    args=parser.parse_args()
    base=os.path.expanduser("~/.local/share/ice/firefox")
    if not os.path.isdir(base):
        print("firefox folder not found at",base)
        return
    for name in os.listdir(base):
        p=os.path.join(base,name)
        if os.path.isdir(p):
            process(p,args.apply)

if __name__=="__main__":
    main()

