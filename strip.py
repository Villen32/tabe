def strip_sade(matn):
    shoro = 0
    payan = len(matn) - 1

   
    while shoro < len(matn) and matn[shoro] == " ":
        shoro = shoro + 1

    
    while payan >= 0 and matn[payan] == " ":
        payan = payan - 1

    jadid = ""
    for i in range(shoro, payan + 1):
        jadid = jadid + matn[i]

    return jadid


kalame = input("ye matn ba space vared kon: ")
print("matn strip sade:", strip_sade(kalame))
