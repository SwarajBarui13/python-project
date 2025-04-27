from time import *
import random as r

def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error=error+1
        except:
            error=error+1
    return error


def speed_time(time_s,time_e,userinput):
    time_delay=time_e-time_s
    time_R=round(time_delay,2)
    speed=len(userinput)/time_R
    return round(speed)



while True:
    a=input("Ready to Test:Yes/No: ")
    if a.lower()=="yes":
        test=["The quick brown fox jumps over the lazy dog is a popular pangram used to test typing skills, but real typing tests involve longer, more complex sentences.Typing is not just about speed; it is also about accuracy and consistency.In today's digital world, efficient typing can enhance productivity and open up a wide range of professional opportunities.Good typing posture includes sitting upright, keeping your wrists elevated, and placing fingers correctly on the home row keys.To improve typing speed, one must practice regularly, focus on common English words, and avoid looking at the keyboardOver time, muscle memory will develop, and typing will become a subconscious action, just like speaking or writing with a pen.Remember, it is better to type slowly and correctly rather than quickly with many mistakes, as accuracy builds a strong foundation for true speed.With perseverance and dedication, anyone can master the art of fast and accurate typing.",
            "Success is not the result of spontaneous combustion; you must set yourself on fire.In every field of endeavor, from business and science to art and athletics, discipline, patience, and relentless effort play a vital role.Those who achieve greatness are often the ones who are willing to persevere through failure, to continue when the excitement fades, and to stay focused on their vision when obstacles appear.Dreams without goals are merely wishes, and goals without plans are merely intentions.True progress comes from setting clear objectives, breaking them into manageable steps, and working on them consistently, even when motivation dwindles.In a rapidly changing world, adaptability, continuous learning, and emotional resilience have become as important as technical skills.Remember, every expert was once a beginner who decided to keep going no matter what.The difference between those who succeed and those who don't often lies in the simple decision to keep moving forward when others give up."]

        test1=r.choice(test)
        print("*****Typing Speed******")
        print(test1)

        print()
        print()
        time_1=time()

        testinput=input("Enter:")
        time_2=time()

        print("Speed:", speed_time(time_1,time_2,testinput),"W/sec")
        print("Error: ",mistake(test1,testinput))
    elif a.lower()=="no":
        print("Thank You")
        break
    else:
        print("Wrong Input")
