import os
import re
import json


configuaration = {
    'version_file': './',
    'template_word': 'VERSION',
    'branch_default': '',
    'changelog_allow': False,
    'changelog_path': './',
    'template_path': './template/template',
    'version_path': './version.c'
}


def parseArguments():
    print("parseArguments")


def getVersionFromVcs():
    """
    request from vcs tag like:
    major.minor.patch[-pre-release][+metadata]-\d+
    and parse it
    """
    myCmd = os.popen('git describe --tags --long').read()

    pattern = r'\d+(\.\d+){2}(-[\w.]+)?(\+[\w.]+)?-\d+'
    match = re.search(pattern, myCmd)
    return match[0] if match else ''


def parseVcsVersion(vs):
    """
    major - only digit require
    minor - only digit require
    patch - only digit require
    pre-release - -[a-zA-Z0-9_\.] optional
    metadata - +[a-zA-Z0-9_\.] optional
    revision - digit require
    """
    match = re.search(
        r'(\d+)\.(\d+)\.(\d+)(?:-([\w.]+))?(?:\+([\w.]+))?-(\d+)',
        vs
        )
    return match.groups()


def buildVersionString(ver):
    """
      0     1      2      3             4       5
    major.minor.patch[-pre-release][+metadata].\d+
    """
    semver = ''
    if ver:
        for (x, item) in list(zip(range(len(ver)), ver)):
            if item:
                sep = '.'
                if x == 0:
                    sep = ''
                elif x == 3:
                    sep = '-'
                elif x == 4:
                    sep = '+'
                semver += sep + item
    else:
        semver = 'fail_version'

    return semver


def getHashFromVcs():
    """get last commit hash and return 10 character"""
    myCmd = os.popen('git show -s --format="%H %ad" --date=short').read()
    print(myCmd)


def saveVersionToBranch():
    print("saveVersionToBranch")


def getVcsLog():
    # git log tagFrom...tagTo --pretty=format:'%h %ad | %s%d [%an]' --graph
    # --date=short | grep "#changelog"
    print("parseArguments")


def archivePrj():
    # git archive ...
    print("archivePrj")


def createChangelog():
    print("createChangelog")


def commitToBranch():
    print("commitToBranch")


def buildVersionFile(cfg):
    ver_striing = getVersionFromVcs()
    match = parseVcsVersion(ver_striing)
    str_ver = buildVersionString(match)
    buildFromTemplate(cfg, str_ver)


def buildFromTemplate(cfg, str_ver):
    template = open(cfg['template_path'], 'r')

    ver_file = open(cfg['version_path'], 'w')

    for line in template:
        line = re.sub(
                '{{' + cfg['template_word'] + '}}',
                str_ver,
                line
            )
        ver_file.write(line)

    template.close()
    ver_file.close()


def readConfig(cfg):
    config_file = open("config.json", "r")
    config = json.load(config_file)
    config_file.close()

    for c in config:
        if c in cfg:
            cfg[c] = config[c]


if __name__ == '__main__':
    readConfig(configuaration)

    buildVersionFile(configuaration)
