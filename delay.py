import time
# አብ ላዕሊ time አእቲና አለና። ጊዚ ጸብጺብካ ንምድንጉአያት ዝሕግዝ
# ድሕሪኡ ልቺ ዝውልዕ function ከፊትና አለና
# አብ ክንዲ ልቺ ምውላዕ ግን ON አብ ስክሪን ክንጽሕፍ ኢና
  
def on():
    print("ON")
      
# ድሕሪኡ ከአ ልቺ ዘጥፍኣ function
# ግን አብ ክንዲ ምጥፋኣ OFF ክንጽሕፍ ኢና።
      
def off():
    print("OFF")

# ከም ሳልሳይ ን ልቺ ውልዕ ጥፍአ ዘብል
# አብዚ x ን ንውሓት ሰከንድታት ዝተዋህበ variable እዩ

def blink(x):
    count = 5 # ን ሓሙሽተ ጊዜ ክንደጋግሞ ኢና። ክንዲ ዝተደልየ ክኸውን ይኽአል
    while count>0:
        count-=1       # ምድግጋም ብሓደ ነጉድሎ
        on()           # ልቺ ንውልዕ
        time.sleep(x)  # ን x ሰክንድታት ደው ንብል (delay)
        off()          # ልቺ ነጥፍእ
        time.sleep(x)  # ን x ሰከንድታት ደው ንብል (delay)
    print("ፕሮግራም ተወዲኡ፡፡")

      
# ነዚ አብ ላዕሊ ዝጸሓፍናዮ ፕሮግራም ንምትግባር 
# ካብ ተጠቃሚ ሰከንድታት ዝቕበል function ይስዕብ
def do_action():
    _sec = input("ክንደይ ሰከንድታት? ")   # ተጠቃሚ ሰከንድታት ክህበና ንሓትት
    try: # ተጠቃሚ ፊደላት አአትዩ ከይከውን ነረጋግጽ
        sec = float(_sec) # ዝተዋህበ ቃል ናብ ተንሳፋፊ ቁጽሪ ንቕይር፣ ምኽንያቱ አታዊ ከም ቃል ጥራይ ኣዩ ዝፍለጥ
        blink(sec)        # አቐዲምና ዝጸሓፍናዮ ውልዕ ጥፍእ ዘብል ፋንክሽን ንጽውዕ

    except: # ተጠቃሚ ዝሃቦ ነገር ቁጽሪ እንተዘይኮይኑ 
        print("ዝተዋህበ ሰከንድታት ብቑዕ አይኮነን") # ዝተዋህበ ነገር ብቑዕ ዘይምኹአኑ ንሕብር
      
# አብ መወዳእታ፣ ብሙሉኡ ፕሮግራም ክትግበር ንጽውዕ
do_action()
