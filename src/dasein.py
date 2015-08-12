import java
import os
import glob

def buildClasspath(jar_path, jar_name):
    classpath = [jar_path + '/' + jar_name]
    dep_path = jar_path + '/lib'
    jars = glob.glob(dep_path + '/*.jar')
    classpath += jars
    return classpath

def execWorkflow(cloud_name, workflow, env={}, args=[]):
    import sys
    sys.path.insert(0, '../config')
    import config

    # get the cloud properties path
    env['DSN_PROPERTIES'] = config.properties_path[cloud_name]

    # build classpath
    classpath = buildClasspath(config.jar_path['nfv'], config.jar_name['nfv'])
    classpath += buildClasspath(config.jar_path[cloud_name], config.jar_name[cloud_name])
    java.execJar(classpath, env, workflow, args)

if __name__ == '__main__':
    cloud_name = 'aws'
    workflow = 'bds.clemson.nfv.workflow.info.ListVMProducts'
    env={'DSN_CMD_ARCHITECTURE':'x86_64'}
    execWorkflow(cloud_name, workflow, env )
