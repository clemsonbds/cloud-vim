import subprocess



def execJar(classpath_arr, env_dict, class_name, args_arr):
    arr = ['java']

    if len(classpath_arr) > 0:
        arr += ['-cp']
        arr += [':'.join(classpath_arr)]

    arr += ['-D' + x + '=' + env_dict[x] for x in env_dict.viewkeys()]
    arr += [class_name]
    arr += args_arr
    print arr
    subprocess.call(arr)

if __name__ == "__main__":
    cp = ['test1', 'test2']
    env = {'DSN_CMD_PRODUCT':'m1.small'}
    cname = 'class'
    args = ['arg1', 'arg2']
    execJar(cp, env, cname, args)
