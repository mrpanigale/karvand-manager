#imports
import json
import os
# variables
path =r"E:\MLprojects\karvand-manager\karvand-manager\data\karvands.json"
# add karvand function✔️
def add_karvand ( user_id: str, full_name: str, city:str,\
                  degree:str, field:str, skill_name:str,\
                skill_level:str, skill_score:int,path:str):
    '''This function add persons to the karvands json file
      if the json file already exists
      but if json file not exists this function
        will call creat json function'''



    # full estructure made by generate karvand function
    karvand = generate_karvand_report( user_id, full_name,\
                                       city, degree, field, skill_name,\
                                     skill_level, skill_score)
    

    #if karvands file exists
    if os.path.exists(path):
        new_person = karvand['karvands'][0]
        with open(path,'r',encoding='utf-8') as file:
            karvand_dictionary = json.load(file)

            karvand_dictionary['karvands'].append(new_person)
        #over write the karvands.json or Update karvands.json
        with open(path,'w') as file:

            json.dump(karvand_dictionary,file,ensure_ascii=False,indent=4)
            print("karvand added.")
    else:
        create_json(karvand,path)
    
# edit karvand function
def edit_karvand (path):...
# show karvand function
def show_karvand (path):
    data = json_reader(path)
    if not data:
        print('file is empty')
        return
    bootcamp = data.get("bootcamp", {})
    karvands_list = data.get("karvands", [])

    print(f"\n{'#'*40}")
    print(f"🎓 BOOTCAMP: {bootcamp.get('title')} ({bootcamp.get('year')})")
    print(f"{'#'*40}")

    for person in karvands_list:
        print(f"🆔 ID: {person.get('id')}")
        print(f"👤 Name: {person.get('full_name')}")
        print(f"📍 City: {person.get('city')}")
        
        edu = person.get("education", {})
        print(f"📚 Education: {edu.get('degree')} in {edu.get('field')}")
        
        print("🛠  Skills:")
        for skill in person.get("skills", []):
            print(f"   - {skill.get('name')} | Level: {skill.get('level')} | Score: {skill.get('score')}")
        
        print(f"{'-'*40}")    
# delet karvand function
def delet_karvand (path):...
# report all karavands function
def report_karvands (path):...
# read json files function
def json_reader (path):
    if os.path.exists(path):
        with open(path,'r') as file:
            karvands_dictionary = json.load(file)
            return karvands_dictionary
    else:
        print("karvands.json did not creat yet!")
# create json file function✔️
def create_json (karvand,path):
    #create and write on karvands.json for first time
    with open(path,'w',encoding='utf-8') as file:
        json.dump(karvand,file,ensure_ascii=False,indent=4)
        print("file craeted and karvand added to the file!")

# generate karavands data✔️
def generate_karvand_report( user_id, full_name, city, degree, field, skill_name, skill_level, skill_score,bootcamp_title='Karvand Python', bootcamp_year='2026'):
    data = {
        "bootcamp": {
            "title": bootcamp_title,
            "year": bootcamp_year
        },
        "karvands": [
            {
                "id": user_id,
                "full_name": full_name,
                "city": city,
                "education": {
                    "degree": degree,
                    "field": field
                },
                "skills": [
                    {
                        "name": skill_name,
                        "level": skill_level,
                        "score": skill_score
                    }
                ]
            }
        ]
    }
    return data


# loop user control panel✔️

while True:
    #flag 
    flag = input('1.Add 2.edit 3.show 4.delet 5.report 6.exit: ')
    #options
    #add✔️
    if flag == '1':
        #inputs
        # TODO: id codes should be unique
        user_id = input('user id: ')
        full_name = input('\n🟰🟰🟰🟰🟰🟰\nfull name: ')
        city = input('\n🟰🟰🟰🟰🟰🟰\ncity: ')
        degree =input('\n🟰🟰🟰🟰🟰🟰\ndegree (like Bachelor): ')
        field = input('\n🟰🟰🟰🟰🟰🟰\nfield (like Computer Engineering)').title()
        skill_name = input('\n🟰🟰🟰🟰🟰🟰\nskill name: (like Python): ').title()
        skill_level = input('\n🟰🟰🟰🟰🟰🟰\nskill level (like beginner): ')
        try:
            skill_score = int(input('\n🟰🟰🟰🟰🟰🟰\nskill score (like 70): '))
        except:
            print('\n🟰🟰🟰🟰🟰🟰\nonly numeric value for score like 1 or 2 or 100 or 70')
            skill_score = int(input('\n🟰🟰🟰🟰🟰🟰\nskill score (like 70): '))

        add_karvand(user_id, full_name, city,degree, field, skill_name, skill_level, skill_score,path=path)


    #edit
    elif flag == '2':
        edit_karvand(path=path)
    #show
    elif flag == '3':
        show_karvand(path=path)
    #delet
    elif flag == '4':
        delet_karvand(path=path)
    #report
    elif flag == '5':
        report_karvands(path=path)
    #exit✔️
    elif flag == "6":
        break
    # unknown input
    else:
        print("Unkonw input!")