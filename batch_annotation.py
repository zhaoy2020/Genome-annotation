# %%
import yaml
import os
# %%
    # =============================================================================
    #     os.listdir()          # 很有用
    #     os.mkdir()
    #     os.remove()
    #     os.rename()
    #     os.getcwd()
    #     os.chdir()
    #     os.path.abspath("a:/just/do/python")
    #     os.path.basename()
    #     os.path.dirname()
    #     os.path.split()
    #     os.path.join()
    #     os.path.exists() # 判断路径是否存在
    #     os.path.isfile()
    #     os.path.isdir()
    #     
    # =============================================================================
# %%
jobsWorkPath = os.path.join(os.getcwd(),'jobs') 
dirs = os.listdir(jobsWorkPath)
counter = 1
for dirName in dirs:
    print(dirName, f'---------{counter}/{len(dirs)}')

    with open(os.path.join(jobsWorkPath, dirName, 'input.yaml'), 'w',encoding='UTF-8') as input_yaml:
        dict_input_yaml = {'fasta':{'class':'File', 'location':dirName+'.fna'}, 
                           'submol': {'class':'File', 'location':'submol.yaml'}}
        yaml.dump(dict_input_yaml, input_yaml, default_flow_style=False)

    with open(os.path.join(jobsWorkPath, dirName, 'submol.yaml'), 'w',encoding='UTF-8') as submol_yaml:
        dict_submol_yaml =  {'organism': {'genus_species': 'Bacillus subtilis', 'strain': dirName},
                             'topology': 'circular',
                             'authors': [{'author': {'first_name': 'Yu', 'last_name': 'Zhao'}}],
                             'contact_info': {'first_name': 'Yu',
                                              'last_name': 'Zhao',
                                              'email': 'zhao_sy@126.com', 
                                              'organization': 'China Agriculture University',
                                              'department': 'College of Plant Protection',
                                              'phone': '', 
                                              'street': '2 Yuanmingyuan West Road, Haidian District, Beijing', 
                                              'city': 'Beijing', 
                                              'postal_code': '100193', 
                                              'country': 'China'}}
        yaml.dump(dict_submol_yaml, submol_yaml, default_flow_style=False)

    cmd = "python /bmp/exp/2019-zhaoyu/WorkStation/pgap/pgap.py -n --no-internet --no-self-update --taxcheck --auto-correct-tax  -o " + os.path.join(jobsWorkPath, dirName,"results") + ' ' + os.path.join(jobsWorkPath, dirName, 'input.yaml')
    # cmd = "python /bmp/exp/2019-zhaoyu/WorkStation/pgap/pgap.py -n --no-self-update --taxcheck --auto-correct-tax  -o " + os.path.join(jobs, i,"results") + ' ' + os.path.join(jobs, i, 'input.yaml')
    # cmd = "python /bmp/exp/2019-zhaoyu/WorkStation/pgap/pgap.py -n   --taxcheck --auto-correct-tax  -o " + os.path.join(jobs, i,"results") + ' ' + os.path.join(jobs, i, 'input.yaml')
    print(cmd)
    os.popen(cmd)   # 并行执行
    # os.system(cmd) # 挨个执行
    
    counter += 1
