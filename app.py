#UI 

from dotenv import load_dotenv
from utils.text_util import clean_transcript
load_dotenv()  

import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


import streamlit as st
from services.audio import extract_audio
from services.transcribe import transcribe
from services.mom_gen import generate_mom



st.title("AI MoM Generator")

uploaded_file = st.file_uploader(
    "Upload meeting recording",
    type=["mp4", "wav", "mp3"]
)


if uploaded_file:
    os.makedirs("temp", exist_ok=True)
    file_path = f"temp/{uploaded_file.name}"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("File uploaded successfully")

    
    audio_path = extract_audio(file_path)
    st.success("Audio extracted")


    with st.spinner("Transcribing audio..."):
        transcript = transcribe(audio_path)

    st.text_area("Transcript", transcript, height=200)


    transcript=" So today we are going to solve this question on our own. So it's like 1 to 4 8 count number of nice subarries. So the question says that given an arrow of integers nums and you are given an integer k. A continuous sub array is called nice if there are k odd numbers on it. So you need to return the number of nice subarries. So we need to return the number of nice subarries over here. Let us see some examples. The first example is like 1, 1, 2, 1, 1 where k is equal to 3. So we need to count those number of subarries which contains 3 odd numbers. So let us see. So for a sub array to contain 3 odd numbers we need at least length 3 of that particular sub array at least. So instead of looking to 1 then like this and like this we will directly look at 3, 3 parts. 3 or more parts. So it's like 1, 1, 2. Is this a valid sub array? No, because it has this only 2 odd numbers. If I increase the length now this is a valid sub array. So our count is 1. And if I increase one more length then also the count is valid. So okay now what I am thinking right now is this is a valid sub array which is written in the explanation as well. And then the other valid sub array they are saying is this. So it's like we need only k odd numbers not more than that. So like this whole array can't be our answer. Right this whole, so this and then this. So 2 sub arrays like that we are having. Coming to the next example 2, 4, 6 and k is 1. So we need at least one odd number. And here in this whole array we don't have a single odd number that's why the count will be 0. Now next one is this where we need 2 odd numbers. So how many sub arrays are possible? So it's like see this could be one sub array. Right? Then this could be another one. And then this could be another one. And then this and then this and then so on. The count will be 16. The count will be 16. Okay. So what is the very first approach coming to our minds? Right? What is the very brute force approach? Since it's about sub arrays we can always count all the sub arrays like we can always look into all the sub arrays. And then while looking into all the sub arrays while I am looking at each sub array I will just count the number of odd numbers in it. If I come across exactly 3 odd numbers in that sub array then only I will count it. Right? So what could be the brute force? It's like I trade for I equals to 0 to n minus 1. Okay? And then we can have a count number let's say. Count variable initialize to 0 for counting the number of odd numbers in this following sub array. So for I equals to 0 to n minus 1 and count equals to 0 then for J equals to 0 to n minus 1. Now what we are going to do is we are going to check. So it's like if A of J is odd, if that particular number is odd then we will do count plus plus. And if that count is equals to K then we will do an answer plus plus. After doing this answer plus plus we could possibly break because further than that we would not need to go further. Is it true? Is it true? Actually we can go further. Why I am saying so? Because I think if you look at this particular sub array it's like you would be able to break after this and then you will not look further but then this is also a valid sub array and this is also a valid sub array. So as long as it is containing K odd numbers it is a valid sub array. So we will not break over here. We will not break over here. We will go up to the full list. We will go up to the full list. Then we will get the answer. Let's see the brute force approach. The length is like up to 10 raised to 4 something. It might work. It might not. Sorry. It might work. It might not but we can at least code the brute force and see if that logic is correct or not. So let me just code the brute force. So it's the same which we discussed. It's like for nt i equals to 0. I will define it over here. n is nums.length and i less than n i plus plus. If we do this we are initializing this variable count. This variable count is to count the number of odd numbers in the sub array. Okay. So we start with our next loop which is j equals to i. j less than n and then this j plus plus. The follow syntax. We are going through the array. If, if nums of j. So it's like number at particular index j. If it's odd we can use a modulo. If it's odd then we will do count plus plus. Right. And if that count is equals to k. If that count is equals to k then we can do n answer plus plus. So for that we need to define and initialize an answer variable as well. Here is the answer variable. Right. And then we will just return this answer. Okay. Let us try to run this code. It is running now. Let us try to submit this code. I don't know whether it might give a tle because it's like the n is up to 10 raised to 4. We are having an overfence square solution. Yeah, as expected. tle is there. tle is there. The time complexity of this solution is like see this will take an overfence. This will also take an overfence all like near about overfence only. So like the complexity of this solution is overfence square. And the space complexity is overfence. If you see the constraints then 10 raised to 4. Right. 5 into 10 raised to 4. If you square it. If I find out 10 raised to 8, so it is little more than 10 raised to 8. That is why it would give tle. Okay. Okay."
    cleaned = clean_transcript(transcript)

    with st.spinner("Generating MoM..."):
        mom = generate_mom(cleaned)

    st.subheader("Minutes of Meeting")
    st.text_area("MoM", mom, height=400)
