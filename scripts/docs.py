import os
import re
import shutil
from os import listdir, path
from os.path import dirname as dn
from pathlib import Path
from typing import Any, Dict, List

import frontmatter
import pdoc
import yaml
from mako.template import Template

from smp import vls

from .settings import stg, wr_stg
from .utils import ddir, inmd, repl, stg

v_ud = '/'.join([str(i) for i in vls[0:2]])

INST_LS = [
    {
        "Index": f"docs/{v_ud}/installation/index.html"
    },
    {
        "Installable": [
            {
                "Index": f"docs/{v_ud}/installation/installable/index.html"
            },
            {
                "Windows 7 and up": f"docs/{v_ud}/installation/installable/windows/index.html"
            },
            {
                "Linux": [
                    {
                        "Index": f"docs/{v_ud}/installation/installable/linux/index.html"
                    },
                    {
                        "Arch": f"docs/{v_ud}/installation/portable/linux/arch/index.html"
                    },
                    {
                        "Debian": f"docs/{v_ud}/installation/portable/linux/debian/index.html"
                    }
                ]
            }
        ]
    },
    {
        "Portable": [
            {
                "Index": f"docs/{v_ud}/installation/portable/index.html"
            },
            {
                "Windows 7 and up": f"docs/{v_ud}/installation/portable/windows/index.html"
            },
            {
                "Linux": [
                    {
                        "Index": f"docs/{v_ud}/installation/portable/linux/index.html"
                    },
                    {
                        "Arch": f"docs/{v_ud}/installation/portable/linux/arch/index.html"
                    },
                    {
                        "Debian": f"docs/{v_ud}/installation/portable/linux/debian/index.html"
                    }
                ]
            }
        ]
    },
    {
        "Programmatic": [
            {
                "Index": f"docs/{v_ud}/installation/programmatic/index.html"
            },
            {
                "Windows 7 and up": f"docs/{v_ud}/installation/programmatic/windows/index.html"
            },
            {
                "MacOS": f"docs/{v_ud}/installation/programmatic/macos/index.html"
            },
            {
                "Linux": [
                    {
                        "Index": f"docs/{v_ud}/installation/programmatic/linux/index.html"
                    },
                    {
                        "Arch": f"docs/{v_ud}/installation/programmatic/linux/arch/index.html"
                    },
                    {
                        "Debian": f"docs/{v_ud}/installation/programmatic/linux/debian/index.html"
                    }
                ]
            }
        ]
    }
]

RE_MD_TPL = r"(?<=# nav {key} start\n).+(?=\n\s+# nav {key} end)"

YML = stg(None, "dev.yml")

DOCS = ddir(YML, "docs")
PDOC = ddir(YML, "pdoc")
MAKO = ddir(YML, "mako")
RULES = ddir(YML, "rules")
MD_VARS_YML = ddir(YML, "md_vars")

RMVC = ddir(MD_VARS_YML, "global")
IDF = Path(f'./{ddir(YML, "docs/input")}')

CONTEXT = pdoc.Context()
PROJECT = pdoc.Module(PDOC["project"], context=CONTEXT)
pdoc.link_inheritance(CONTEXT)

GEN = {
    "docs": [[], []],
    "mako": [[], []],
    "pdoc": [[], []],
}

class Constants:
    pass

def dd(od: Dict[str, List[str]], *dicts: List[Dict[str, List[str]]]) -> Dict[str, List[str]]:
    for d in dicts:
        for a, v in d.items():
            od[a] = [*(od.get(a, []) or []), *v]
    return od

def rules_fn(rules: Dict[Any, Any]) -> Dict[str, List[str]]:
    return dd({"": ddir(rules, "del", [])}, ddir(rules, "repl"))

def docs_dir(mn: str, absolute: bool=True, api: bool=False) -> str:
    mls = mn.split(".")
    if (len(mls) == 1) and (PDOC["project"] == mls[0]):
        mls[0] = "index"
    elif (len(mls) >= 2) and (PDOC["project"] == mls[0]):
        del mls[0]
    rel_ls = [
        *[str(i) for i in vls[0:2]],
        *mls[:-1],
        f"{mls[-1]}.md"
    ]
    if api:
        rel_ls.insert(2, "api")
        rel_ls.insert(0, "docs")
    rel = path.join(*rel_ls)
    abs = path.join(PDOC["op"], rel)
    GEN["pdoc"][1].append(abs)
    inmd(abs, GEN["pdoc"][0])
    if absolute:
        return abs
    else:
        return rel

def yield_text(mod):
    yield mod.name, mod.text()
    sm = {}
    for submod in mod.submodules():
        sm[submod.name] = docs_dir(submod.name, api=True)
        yield from yield_text(submod)

    if sm:
        if sum:=mod.supermodule:
            sum = f"\n\n## Super-module\n- [{sum.name}]({docs_dir(sum.name, False)})\n"
        else:
            sum = ""

        smls = []
        for k, v in sm.items():
            v = "/".join(v.split("/")[5:])
            smls.append(f'- [{k}]({v})')
        sm = "\n\n## Sub-modules\n\n{}\n".format("\n".join(smls))

        idx = """# {}{}{}""".format(
            mod.name,
            sum,
            sm,
        )

        idx_path = docs_dir(mod.name, api=True)
        with open(idx_path, "w") as f:
            f.write(idx)

def del_gen():
    try:
        for _, v in stg("generated", "docs/_meta.yml").items():
            for i in v["folders"]:
                if path.isdir(i):
                    shutil.rmtree(i)
            for i in v["files"]:
                if path.isfile(i):
                    os.remove(i)
    except TypeError:
        shutil.copy("docs/_meta.yml.bak", "docs/_meta.yml")
        del_gen()

def main(rmv: Dict[Any, Any]={}, hr :bool=False):
    docs_pdir = DOCS["op"]
    rmv_r = ddir(rmv, "rules")
    rmv_mv = ddir(rmv, "md_vars")
    MVC = dict(RMVC, **ddir(rmv_mv, "global"))

    del_gen()

    for rip in list(IDF.rglob("*.ymd")):
        out = path.join(
            docs_pdir,
            *rip.parts[1:-1],
            f"{rip.stem}.md"
        )
        GEN["docs"][1].append(out)

        rf = frontmatter.load(rip)
        md = repl(rf.content, dd(rules_fn(RULES), rules_fn(rmv_r)))

        d = {
            **MVC,
            **ddir(
                MD_VARS_YML,
                f"local/{rip.stem}"
            ),
            **ddir(
                rmv_mv,
                f"local/{rip.stem}"
            )
        }
        for k, v in {k: str(v) for k, v in d.items()}.items():
            md = md.replace(f"${{{k}}}", v)

        if title:=rf.get("title"):
            if link:=rf.get("link"):
                md = """<h1 align="center" style="font-weight: bold">
    <a target="_blank" href="{}">{}</a>
</h1>\n\n{}\n""".format(link, title, md)
            else:
                md = """<h1 align="center" style="font-weight: bold">
    {}
</h1>\n\n{}\n""".format(title, md)

        with open(inmd(out, GEN["docs"][0]), "w") as f:
            f.write(md)

    for module_name, yt in yield_text(PROJECT):
        _dd = docs_dir(module_name, api=True)
        with open(_dd, "w") as f:
            f.write(yt)
        GEN["pdoc"][1].append(_dd)

    for pip in list(IDF.rglob("*.mako")):
        ip = str(pip)
        with open(ip, "r") as f:
            iprl = f.readline()
        if iprl != "## ignore\n":
            op = path.join(
                docs_pdir,
                *pip.parts[1:-1],
                f"{pip.stem}.md"
            )
            mytemplate = Template(filename=ip)
            tpl_rd = mytemplate.render(
                **{
                    "cwd": Path(dn(ip)),
                    "VARS": {
                        **MVC,
                        **ddir(
                            MD_VARS_YML,
                            f"local/{pip.stem}"
                        ),
                        **ddir(
                            rmv_mv,
                            f"local/{pip.stem}"
                        )
                    },
                }
            )
            with open(inmd(op, GEN["mako"][0]), "w") as f:
                f.write(tpl_rd)
            GEN["mako"][1].append(op)

    shutil.copy("docs/_meta.yml", "docs/_meta.yml.bak")
    for k, v in GEN.items():
        for key, i in zip(["folders", "files"], v):
            wr_stg(f"generated/{k}/{key}", list(set(i)), "docs/_meta.yml")

    if not hr:
        base = path.join("raw_docs", "docs")

        ndd = {}
        for u in listdir(base):
            for d in listdir(path.join(base, u)):
                ndd[f"{u}.{d}"] = f"docs/{u}/{d}/index.html"

        lk = list(ndd.keys())[-1]
        ndd[f'{lk} (Current)'] = ndd.pop(lk)
        nd = yaml.dump(ndd, default_flow_style=False)
        nd = "\n".join([f'    - {i}' for i in nd.strip().split("\n")][::-1])

        p_inst_ls = yaml.dump(INST_LS, default_flow_style=False)
        p_inst_ls = "\n".join([f'    {i}' for i in p_inst_ls.strip().split("\n")])

        with open("mkdocs.yml", "r") as f:
            mkdocs = f.read()

        mkdocs = re.sub(RE_MD_TPL.format(key="docs"), nd, mkdocs, 1, flags=re.DOTALL)
        mkdocs = re.sub(RE_MD_TPL.format(key="inst"), p_inst_ls, mkdocs, 1, flags=re.DOTALL)

        with open("mkdocs.yml", "w") as f:
            f.write(mkdocs)
        shutil.copy("mkdocs.yml", "mkdocs.yml.bak")
