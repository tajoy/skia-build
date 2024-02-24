#! /usr/bin/env python3

import common, json, sys, urllib.request

def main():
  headers = common.github_headers()
  version = common.version()
  build_type = common.build_type()
  system = common.system()
  machine = common.machine()
  classifier = common.classifier()
  
  try:
    resp = urllib.request.urlopen(urllib.request.Request('https://api.github.com/repos/tajoy/skia-build/releases/tags/' + version, headers=headers)).read()
    artifacts = [x['name'] for x in json.loads(resp.decode('utf-8'))['assets']]
    zip = 'Skia-' + version + '-' + system + '-' + build_type + '-' + machine + classifier + '.zip'
    if zip in artifacts:
      print('> Artifact "' + zip + '" exists, stopping')
      return 1
    return 0
  except urllib.error.URLError as e:
    return 0

if __name__ == '__main__':
  sys.exit(main())
