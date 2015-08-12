
def main():
    import sys
    sys.path.insert(0, '../src')
    import dasein

    cloud = 'aws'
    workflow = 'bds.clemson.nfv.workflow.info.ListVMProducts'
    env = {
        'DSN_CMD_ARCHITECTURE':'x86_64'
    }

    dasein.execWorkflow(cloud, workflow, env)

if __name__ == "__main__":
    main()
