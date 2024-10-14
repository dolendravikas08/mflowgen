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
FLOORPLAN_ODB = RESULTS_DIR + '/floorplan_output.odb'
FLOORPLAN_SDC = RESULTS_DIR + '/floorplan_output.sdc'

# prepare next file inputs
if next_step == '5-orfs-openroad-power':
  POWER_INPUT_ODB = RESULTS_DIR + '/power_input.odb'
  POWER_INPUT_SDC = RESULTS_DIR + '/power_input.sdc'

  shutil.copy(FLOORPLAN_ODB, POWER_INPUT_ODB)
  print(f"Copied {FLOORPLAN_ODB} to {POWER_INPUT_ODB}")

  shutil.copy(FLOORPLAN_SDC, POWER_INPUT_SDC)
  print(f"Copied {FLOORPLAN_SDC} to {POWER_INPUT_SDC}")

