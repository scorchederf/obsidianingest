import requests

def check_availability(name, platform):
    if platform == "twitter":
        response = requests.get(f"https://twitter.com/{name}")
        return not response.ok
    elif platform == "reddit":
        response = requests.get(f"https://www.reddit.com/user/{name}/about.json")
        return response.status_code == 404
    elif platform == "youtube":
        response = requests.get(f"https://www.youtube.com/user/{name}")
        return "channel-not-found" in response.text
    elif platform == "github":
        response = requests.get(f"https://github.com/{name}")
        return response.status_code == 404
    else:
        return False

def verify_names(names):
    available_names = []
    for name in names:
        print ("checking " + name)
        if (
            check_availability(name, "twitter")
            and check_availability(name, "reddit")
            and check_availability(name, "youtube")
            and check_availability(name, "github")
        ):
            print ("found one: " + name)
            available_names.append(name)
    return available_names

# Example usage:
names_to_verify = ["4lph4Str1k3","N3bul4G4z3r","4rc4n3Bl1tz","5h4d0wV0rt3x","N0v4FurY","Ph4nt0m5l4y3r","C3l35t14lGl1d3","5p3ctr4lR34p3r","V3n0m0u5Sh4d3","3cl1ps3Pul53","4zur3T3mp3st","Bl1tzkr13gXpl0r3r","R0gu3Wh1sp3r","R4d14nt50rc3r3r","3mb3rDr1ft3r","Lun4rQu454r","5t33lN0v4","Cr1m50nR4pt0r","V01dG4z3r","1gn15Dr1ft3r","Thund3rN0v4","53rp3ntGl1mm3r","N0v45h4d0w","30nBl1zz","Ph03n1xBl4d3","N1mbu5FurY","4by55alKn1ght","5113nt5tr1k3r","3t3rn4lR34p3r","5p4rt4nGl1d3","NyXG4z3r","V3n0mQu454r","Bl4z3T3mp3st","4str4lStr1k3","54b3rV0rt3x","V1p3rPul53","5h4d0wFurY","Cr1m50nDr1ft3r","1nf3rn0S0rc3r3r","R4p1dN0v4","Ph4nt0mR4pt0r","Lun4r3cl1p53","30nWh1sp3r","N3bul4Sh4d3","4zur3Str1k3","5p3ctr41Bl1tz","3mb3rV0rt3x","4str4lQu4k3","NyXGl1mm3r","V3n0m0u5Bl4d3","51l3ntN0v4","5t33lG4z3r","Thund3r5h4d0w","Ph03n1xR34p3r","N1mbu5Sl4y3r","4by55alWr41th","R4d14ntGl1d3","3t3rn4lWh1sp3r3r","5p4rt4nPul53","1nf3rn0Qu4k3","R4p1dT3mp3st"]
available_usernames = verify_names(names_to_verify)

print("Available usernames:")
print(available_usernames)