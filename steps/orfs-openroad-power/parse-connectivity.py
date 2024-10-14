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
POWER_ODB = RESULTS_DIR + '/power_output.odb'
POWER_SDC = RESULTS_DIR + '/power_output.sdc'

if next_step == '6-orfs-openroad-place':
  PLACE_INPUT_ODB = RESULTS_DIR + '/place_input.odb'
  PALCE_INPUT_SDC = RESULTS_DIR + '/place_input.sdc'

  shutil.copy(POWER_ODB, PLACE_INPUT_ODB)
  print(f"Copied {POWER_ODB} to {PLACE_INPUT_ODB}")

  shutil.copy(POWER_SDC, PALCE_INPUT_SDC)
  print(f"Copied {POWER_SDC} to {PALCE_INPUT_SDC}")

