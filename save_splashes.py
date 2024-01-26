import pickle
#i have not a single idea in the slightest what am i doing

wakeup_splashes = [
    "Hello gordon",
    "It's me Gordon, Barney from Black Mesa",
    "Powerup initiated.",
    "hello i am awake and it's currently {datetime.now().strftime('%H:%M')}",
    "hello this is a wake up splash",
    ]

wakeup_splashes_descriptions = [
    "half life",
    "half life 2",
    "portal 2",
    "original quote by me",
    "original quote by me",
]

splashes = [
    "Hello, and again, welcome to the Aperture Science Enrichment Center. We are currently experiencing technical difficulties due to circumstances of potentially apocalyptic significance beyond our control. However, thanks to Emergency Testing Protocols, testing can continue. These pre-recorded messages will provide instructional and motivational support, so that science can still be done, even in the event of environmental, social, economic, or structural collapse.",
    "hello i just wanted to tell you <@318571303881801728> can go kys i hate him",
    "hello i just wanted to tell you <@691598832273850440> can go kys i hate him",
    "hello i just wanted to tell you <@795404576839958529> can go kys i hate him",
    "hello i just wanted to tell you <@735971349973172355> can go kys i hate him",
    "Also try icosahedron!",
    "Also try ammeter!",
    "did i leak my token",
    "nevermind",
    "welcome to the caterture science worship-aided catching center\nWe hope your brief detention in the relaxation vault has been a pleasant one.\nYour worships have been sumbitted and now we can begin the catching proper.\nBefore we start, however, keep in mind that although fun and profit are the primary goals of all catching center activities, serious injuries may occur. \nFor your own safety and the safety of others, please refrain from touching \n[inaudible] \nstand back. The cat will appear in three. two. one.",
    "antiragraba 🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏",
    "ампержопа ты тут?",
    "ампержопаааааааааааааааааа",
    "currently {len(splashes)} splashes",
]
splashes[splashes.index("currently {len(splashes)} splashes")]=f"currently {len(splashes)} splashes"

splashes_descriptions = [
    "Portal 2",
    "quote of me",
    "quote of me except i put goober's id",
    "quote of me except i put tdm's id",
    "quote of me except i put tintin's id",
    "Also try icosahedron!",
    "Also try ammeter!",
    "-ammeter",
    "nvm",
    "https://discord.com/channels/1162827693075746876/1172983850587148348/117298385058714834",
    "a misspelled inside joke",
    "idk what to type here",
    "idk what to type here",
    "just a splash counter",
]

pickle.dump(wakeup_splashes, open("wakeup.dat", "wb"))
pickle.dump(wakeup_splashes_descriptions, open("wakeup_descriptions.dat", "wb"))
pickle.dump(splashes, open("splashes.dat", "wb"))
pickle.dump(splashes_descriptions, open("splashes_descriptions.dat", "wb"))