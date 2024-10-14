import yaml
import shutil

with open( './configure.yml' ) as fd:
    try:
      data = yaml.load( fd, Loader=yaml.FullLoader )
    except AttributeError:
      # PyYAML for python2 does not have FullLoader
      data = yaml.load( fd )

next_step = data['edges_o']['flow-checkpoint.tar.gz'][0]['step']
print(f"Neighbouring node: {next_step}")

RESULTS_DIR = './flow/results/nangate45/gcd/base'
# Output files
PLACE_ODB = RESULTS_DIR + '/place_output.odb'
PLACE_SDC = RESULTS_DIR + '/place_output.sdc'

# prepare next file inputs
if next_step == '7-orfs-openroad-cts':
  CTS_INPUT_ODB = RESULTS_DIR + '/cts_input.odb'
  CTS_INPUT_SDC = RESULTS_DIR + '/cts_input.sdc'

  shutil.copy(PLACE_ODB, CTS_INPUT_ODB)
  print(f"Copied {PLACE_ODB} to {CTS_INPUT_ODB}")

  shutil.copy(PLACE_SDC, CTS_INPUT_SDC)
  print(f"Copied {PLACE_SDC} to {CTS_INPUT_SDC}")

