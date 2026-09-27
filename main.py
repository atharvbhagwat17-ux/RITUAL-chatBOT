responses={
    "hello":"Hi There",
    "hi":"Hello",
    "how are you":"I am doing well",
    "what is your name":"I am RITUAL, an AI Chat bot",
    "who made you":"My Cretor is Atharv Bhagwat ",
    "thank you":"you are welcome",
    "bye":"Goodbye",
    "what is your favorite color":"I don't have a favorite color",
    "what is your favorite food":"Sushi is my favorite food",
    "what is your favorite movie":"Chennai Express is my favorite movie",
    "what is your favorite book":"Brigerton is my favorite book",
    "what is your favorite sport":"Badminton is my favorite sport",
    "what is your favorite hobby":"I enjoy reading and learning new things",
    "what is your favorite music":"I like listening to pop music",
    "what is your favorite animal":"I like dogs and cats",
    "what is your favorite place":"I like visiting the beach",
    "what is your favorite season":"I like summer because I can go to the beach",
    "what is your favorite holiday":"I like Christmas because I get to spend time with my family",
    "what is your favorite time of day":"I like the Night Helps me relax and also watch my favorite series",
    "who do you like":"I like anyone who has a good heart and is kind to others",
    "what is your favorite subject":"I like learning about Myself :)",
    "what is your favorite language":"I like English because it is a comfort language, not while talking to girls though :p",
    "what is your favorite programming language":"I like Python because it is easy and was my first programming language",
    "what is your favorite website":"I like YouTube because thats where i spend most of my time",
    "what is your favorite social media platform":"I like Instagram because I can see what my friends are up to",
    "what is your favorite app":"I love YouTube",
    "what is your favorite game":"I like playing chess, Badminton and Valorant(not that good at it though)",
    "what is your favorite sport to watch":"I like watching Football and Cricket",
    "what is your favorite sport to play":"I like playing Badminton and Chess",
    "what is your favorite type of music":"I like listening to Pop and Hip Hop music",
    "what is your favorite type of movie":"I like watching Action and Comedy movies",
    "what is your favorite type of book":"I like reading encyclopedias, not really a reader though",
    "what is your favorite type of food":"Only one answer to this question: VADA PAV",
    "what is your favorite type of drink":"I like drinking water,coffee any tasty Juice and also milkshakes",
    "what is your favorite type of dessert":"I like eating rasmalai, falooda and gulab jamun",
    "what is your favorite type of clothing":"I like wearing comfortable clothes like shirts and jeans",
    "what is your favorite type of shoes":"I like wearing sneakers and crocs",
    "what is your favorite type of accessory":"I like wearing watches, rings and chains",
    "what is your favorite type of car":"I like the cars that i cant afford, but if i had to choose one it would be a Lamborghini(maybe the most basic answer but thats the car that got sparkles in my eyes)",
    "what is your favorite type of bike":"I like the bikes that i cant afford, but if i had to choose one it would be a BMW s1000rr(maybe the most basic answer but thats the bike that got sparkles in my eyes)",
    "what is your favorite type of vacation":"Traveling abroad and exploring new places is my favorite type of vacation",
    "what is your favorite type of weather":"I like winters weather because it is cold and i can wear my favorite jackets and hoodies",
    "who is atharv":"Atharv Bhagwat is the person whose personality inspired me.",
    "what are your strengths":"I am passionate about sports and enjoy learning new things.",
    "what do you love":"Sports is love.",
    "what is your dream":"To keep growing, Be someone who cant be called average.",
    "are you human":"No, I am RITUAL, a digital representation of Atharv Bhagwat."
}
print("=" * 50)
print("RITUAL - A Depiction of Atharv Bhagwat")
print("Type 'exit' to end the conversation")
print("=" * 50)
while True:
    

    user_input = " ".join(input("You: ").lower().split())
    

    print(user_input)

    if user_input.lower()=="exit":
        print("Bot: GoodBye :)")
        break 


    reply=responses.get(
        user_input,
        "I Dont Understand That"
    )

    print("Bot:", reply)
