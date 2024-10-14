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
CTS_ODB = RESULTS_DIR + '/cts_output.odb'
CTS_SDC = RESULTS_DIR + '/cts_output.sdc'

# prepare next file inputs
if next_step == '8-orfs-openroad-route':
  ROUTE_INPUT_ODB = RESULTS_DIR + '/route_input.odb'
  ROUTE_INPUT_SDC = RESULTS_DIR + '/route_input.sdc'

  shutil.copy(CTS_ODB, ROUTE_INPUT_ODB)
  print(f"Copied {CTS_ODB} to {ROUTE_INPUT_ODB}")

  shutil.copy(CTS_SDC, ROUTE_INPUT_SDC)
  print(f"Copied {CTS_SDC} to {ROUTE_INPUT_SDC}")

