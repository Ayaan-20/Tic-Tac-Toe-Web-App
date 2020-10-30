import streamlit as st

# v = ●
# Making the layout of the page
st.beta_set_page_config(page_title='TIC TAC TOE', page_icon='💠', layout='wide', initial_sidebar_state='collapsed')

# Sidebar layout
st.sidebar.header('MENU 🔘')
selection = st.sidebar.selectbox('', ['Home 🏠', 'TIC TAC TOE 💠', 'About 📜'])

# Home page layout
if selection == 'Home 🏠':
    # Background colour and fonts made by using html
    # 1st box using html
    home_info = '''<div
     style="background-color:#4286f4;padding:10px;border-radius:15px">
    <h2 
    style="color:white;text-align:center;font-size:20px"> TIK TAC TOE : PLAY WITH YOUR FRIENDS ☺️ <BR> A SIMPLE FUN 
    GAME WHICH YOU CAN PLAY INFINITE TIMES FOR FREE !!!! 😍
    </h2> 
    </div> '''
    st.markdown(home_info, unsafe_allow_html=True)
    st.text('')

    # 2nd box using html
    home_info1 = '''<div
    style="background-color:white;padding:20px;border-radius:30px"> 
    <h2 
    style="color:black;text-align:center;font-size:20px">SIMPLE STEPS TO PLAY THE GAME :<BR> <BR>● CLICK THE ARROW ON 
    THE TOP LEFT CORNER , THEN FROM MENU SELECT TIC TAC TOE<BR>● CHOOSE WHICH MARKER YOU WANT "X" OR "O".<BR>● THERE 
    IS A TEMPLATE WHICH SHOWS YOU WHICH N0.TO ENTER TO CHOOSE THE CORRESPONDING CHOICE. <br> 🔴 THEN START PLAYING 🔴 
    </h2> 
    </div> '''
    st.markdown(home_info1, unsafe_allow_html=True)

    # 3rd box using html
    home_info2 = '''<div
     style="background-color: #4AC29A;padding:10px;border-radius:100px">
     <h2 
    style="color:white;text-align:center;font-size:20px"> TO PLAY AGAIN REFRESH THE PAGE 🖱️
    </h2> 
    </div> '''
    st.text('')
    st.markdown(home_info2, unsafe_allow_html=True)

    # 4th box to make the page look vibrant using html
    st.text('')
    fun1 = '''<div
       style="background-color: tomato;padding:10px;border-radius:20px">
       <h2 
       style="color:white;text-align:center;font-size:20px">✖️<BR>✖️✖️<BR>✖️✖️️✖️<BR>✖️ ━━━️ ✖️
       </h2> 
       </div> '''
    st.markdown(fun1, unsafe_allow_html=True)

# About page layout
elif selection == 'About 📜':

    # simple html code to make the page vibrant
    about_info1 = '''<div
    style="background-color:tomato;padding:10px;border-radius:9px">
    </div> '''

    st.markdown(about_info1, unsafe_allow_html=True)

    # writing the text using html
    st.text('')
    about_info2 = '''<div
    style="background-color:white;padding:10px;border-radius:9px">
    <h2 
    style="color:black;text-align:center;font-size:20px">DEVELOPER : AYAAN IZHAR
    </h2> 
    </div> '''
    st.markdown(about_info2, unsafe_allow_html=True)
    st.text('')

    # simple html code to make the page vibrant
    about_info3 = '''<div
    style="background-color:tomato;padding:10px;border-radius:9px">
    </div> '''
    st.markdown(about_info3, unsafe_allow_html=True)
    st.text('')

    # git hub link in the form of button
    st.header('Link - '+'[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat&logo=github)](https://github.com/Ayaan-20)')

    more_about = st.button('● More to know ● ')
    if more_about:

        more = '''<div
        style="background-color: white;padding:10px;border-radius:20px"> 
        <h2 
        style="color:black;text-align:start;font-size:20px">I am a high school python programmer and this is my first 
        web app. I hope you like it !<BR><BR> Special thanks to Streamlit .🤗
        </h2> 
        </div> '''
        st.markdown(more, unsafe_allow_html=True)


# MAIN TIC TAC TOE GAME
elif selection == 'TIC TAC TOE 💠':

    # Using dictionary for easier construction of the board as well as the logic
    # The value is set to "__" as it is going to help in the construction of the board
    tic_tac_board = {'1': '__', '2': '__', '3': '__',
                     '4': '__', '5': '__', '6': '__',
                     '7': '__', '8': '__', '9': '__'}

    # Main heading for the game using html
    tic_tac_selected = '''<div
    style="background-color:#4286f4;padding:10px;border-radius:15px">
    <h2 
    style="color:white;text-align:center;font-size:20px"> 🤩 TIC TAC TOE 🤩
    </h2>
    </div> '''
    st.markdown(tic_tac_selected, unsafe_allow_html=True)
    st.text('')

    # The board
    def displayBoard(board):

        # columns so that the board is aligned correctly
        pl1, pl2, pl3, pl4 = st.beta_columns(4)

        # Template for reference
        pl1.text('━━━━━━━━━━━━━━━━━━━━━━━━')
        pl1.text('1 | 2 | 3')
        pl1.text('')
        pl1.text('4 | 5 | 6')
        pl1.text('')
        pl1.text('7 | 8 | 9')
        pl1.text('━━━━━━━━━━━━━━━━━━━━━━━━')
        pl1.markdown('### TEMPLATE ↑')

        # Board for TIC TAC TOE
        pl2.text('━━━━━━━━━━━━━━━━━━━━━━━━━')
        pl2.text('┃ .' + board['1'] + '. ┃ .' + board['2'] + '. ┃ .' + board['3'] + '. ┃')
        pl2.text('')
        pl2.text('┃ .' + board['4'] + '. ┃ .' + board['5'] + '. ┃ .' + board['6'] + '. ┃')
        pl2.text('')
        pl2.text('┃ .' + board['7'] + '. ┃ .' + board['8'] + '. ┃ .' + board['9'] + '. ┃')
        pl2.text('━━━━━━━━━━━━━━━━━━━━━━━━━')
        pl2.markdown('### 💠 BOARD 💠 ')

    # The main logic of the game
    def game():
        # Putting the whole logic program into the try except blocks so it doesn't show any error in the streamlit page
        try:
            # choice to choose between the marker "X" and "O"
            player_marker = st.selectbox("WHICH MARKER DO YOU NEED PLAYER 1 ? 'X' OR 'O' : ", ['✖️', '⭕'])

            # Assigning the turn according to the choice from the user between the markers.
            if player_marker == '✖️':
                turn = '✖️'
            else:
                turn = '⭕'

            # Keeping count of the turns that user did
            chance_counter = 0

            # Giving user 9 chances as the board consist of 9 places
            i = 0
            while i < 10:
                displayBoard(tic_tac_board)
                # Displaying which player turn is it
                # For user who decides to choose the marker "X"
                if player_marker == '✖️':
                    if turn == '✖️':
                        st.success("Player 1 turn : " + '✖️' + ". Move to which place ?")
                    else:
                        st.warning("Player 2 turn : " + '⭕' + ". Move to which place ?")

                # For user who decides to choose the marker "O"
                else:
                    if turn == '⭕':
                        st.success("Player 1 turn :" + '⭕' + ". Move to which place ?")
                    else:
                        st.warning("Player 2 turn :" + '✖️' + ". Move to which place ?")

                # User's choice to move to which place
                players_move = st.text_input(f'TURN {i + 1}')

                # Making exceptions so that the numbers cannot be entered below 1 and greater than 9
                if int(players_move) > 9 or players_move == '0':
                    st.info('The Number entered should be between 1 and 9. :: check the template ::')

                # updating the value in the board according to which key the user has entered
                if tic_tac_board[players_move] == '__':
                    tic_tac_board[players_move] = turn

                    # Updating counter
                    chance_counter += 1

                    # Incrementing the value of i as this is taken as a turn
                    i += 1

                # If the user has entered the same key again displaying this
                else:
                    st.error('NO.' + players_move + " place is already filled. Choose any other place ?")

                # Making a if condition as there can be a winner only after 4 chances
                if chance_counter >= 5:

                    # Upper row winning condition
                    if tic_tac_board['1'] == tic_tac_board['2'] == tic_tac_board['3'] != '__':
                        displayBoard(tic_tac_board)
                        if turn == '✖️':
                            st.text("\nGame Over for : " + '⭕ 😭')
                        else:
                            st.text("\nGame Over for : " + '✖️ 😭')
                        st.text("❖❖❖❖" + turn + " won. ❖❖❖❖")
                        break

                    # Middle row winning condition
                    elif tic_tac_board['4'] == tic_tac_board['5'] == tic_tac_board['6'] != '__':
                        displayBoard(tic_tac_board)

                        if turn == '✖️':
                            st.text("\nGame Over for : " + '⭕ 😭')
                        else:
                            st.text("\nGame Over for : " + '✖️ 😭')
                        st.text("❖❖❖❖" + turn + " won. ❖❖❖❖")
                        break

                    # Lower row winning condition
                    elif tic_tac_board['7'] == tic_tac_board['8'] == tic_tac_board['9'] != '__':
                        displayBoard(tic_tac_board)

                        if turn == '✖️':
                            st.text("\nGame Over for : " + '⭕ 😭')
                        else:
                            st.text("\nGame Over for : " + '✖️ 😭')
                        st.text("❖❖❖❖" + turn + " won. ❖❖❖❖")
                        break

                    # Left column winning condition
                    elif tic_tac_board['1'] == tic_tac_board['4'] == tic_tac_board['7'] != '__':
                        displayBoard(tic_tac_board)

                        if turn == '✖️':
                            st.text("\nGame Over for : " + '⭕ 😭')
                        else:
                            st.text("\nGame Over for : " + '✖️ 😭')
                        st.text("❖❖❖❖" + turn + " won. ❖❖❖❖")
                        break

                    # Middle column winning condition
                    elif tic_tac_board['2'] == tic_tac_board['5'] == tic_tac_board['8'] != '__':
                        displayBoard(tic_tac_board)

                        if turn == '✖️':
                            st.text("\nGame Over for : " + '⭕ 😭')
                        else:
                            st.text("\nGame Over for : " + '✖️ 😭')
                        st.text("❖❖❖❖" + turn + " won. ❖❖❖❖")
                        break

                    # right column winning condition
                    elif tic_tac_board['3'] == tic_tac_board['6'] == tic_tac_board['9'] != '__':
                        displayBoard(tic_tac_board)

                        if turn == '✖️':
                            st.text("\nGame Over for : " + '⭕ 😭')
                        else:
                            st.text("\nGame Over for : " + '✖️ 😭')
                        st.text("❖❖❖❖" + turn + " won. ❖❖❖❖")
                        break

                    # Diagonal1 winning condition
                    elif tic_tac_board['3'] == tic_tac_board['5'] == tic_tac_board['7'] != '__':
                        displayBoard(tic_tac_board)

                        if turn == '✖️':
                            st.text("\nGame Over for : " + '⭕ 😭')
                        else:
                            st.text("\nGame Over for : " + '✖️ 😭')
                        st.text("❖❖❖❖" + turn + " won. ❖❖❖❖")
                        break

                    # Diagonal2 winning condition
                    elif tic_tac_board['1'] == tic_tac_board['5'] == tic_tac_board['9'] != '__':
                        displayBoard(tic_tac_board)
                        if turn == '✖️':
                            st.text("\nGame Over for : " + '⭕ 😭')
                        else:
                            st.text("\nGame Over for : " + '✖️ 😭')
                        st.text(" ❖❖❖❖ " + turn + " won. ❖❖❖❖")
                        break

                # Tie condition
                if chance_counter == 9:
                    displayBoard(tic_tac_board)
                    st.markdown("### GAME OVER.\n")
                    st.markdown("### It's a TIE !!!")
                    break

                # changing the Turn from "X" to "O" and vice versa
                if turn == '✖️':
                    turn = '⭕'
                else:
                    turn = '✖️'

            # "play again" text made using html
            home_inf1 = '''<div
            style="background-color:#BDFFF3;padding:10px;border-radius:15px">
            <h2 
            style="color:black;text-align:center;font-size:20px"> TO PLAY AGAIN 🤩 :- REFRESH THE PAGE 🖱️
            </h2> 
            </div> '''
            st.markdown(home_inf1, unsafe_allow_html=True)
            st.text('')

            # Popping balloons for fun
            st.balloons()

            # making a button for balloons
            ref1, ref2, ref3 = st.beta_columns(3)
            ref2.button('🎈 BALLOONS 🎈')

        except Exception:
            pass

    game()
