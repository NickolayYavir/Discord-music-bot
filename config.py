BOT_PREFIX = ">"

AUDIOPLAYER_UI = True

BUTTON_PREV_SYMBOL = "|◁"
BUTTON_PLAY_SYMBOL = "▶"
BUTTON_PAUSE_SYMBOL = "❚❚"
BUTTON_SKIP_SYMBOL = "▷|"
BUTTON_LOOP_SYMBOL = "↺"
BUTTON_KILL_SYMBOL = "💀"

SLASH_COMMANDS = False
MIX_SONGS_LIMIT = 25

PLAY_COMMAND_BRIEF = "Play music in a voice channel"
LOOP_COMMAND_BRIEF = "Loop the currently playing song"
SKIP_COMMAND_BRIEF = "Play the next song in the playlist"
PREV_COMMAND_BRIEF = "Play the previous song in the playlist"
PAUSE_COMMAND_BRIEF = "Pause audio in voice channel"
RESUME_COMMAND_BRIEF = "Resume audio in voice channel"
PLAYLIST_COMMAND_BRIEF = "Get a list of songs from the playlist"
STOP_COMMAND_BRIEF = "Stop audio and disconnect from voice channel"

PLAY_COMMAND_DESCRIPTION = f"This command plays music in a voice channel. To use it, type the command followed by a valid YouTube video or playlist link. The bot will check if you are in a voice channel and if the bot is already playing music in the different channel. If not, it will connect to the voice channel and start playing the song. If the bot is already playing music, the command will add the song to the playlist.\n\nRequirements: This command can only be used in a server (not in DMs).\nExamples:\n{BOT_PREFIX}play https://www.youtube.com/watch?v=dQw4w9WgXcQ: Plays the song with the given YouTube link.\n{BOT_PREFIX}play: Sends an error message indicating that a YouTube link is required.\n{BOT_PREFIX}play https://www.youtube.com/watch?v=dQw4w9WgXcQ (while bot is already playing music in the different channel): Sends an error message indicating that the bot is already playing music in another channel.\n{BOT_PREFIX}play https://www.youtube.com/playlist?list=PL8R4u0UAeAo3FisFJfsUuYFTIBcyDk1ti  Plays the playlist with the given YouTube link"
LOOP_COMMAND_DESCRIPTION = "This command allows users to loop the currently playing song. If the loop mode is on, the bot will repeat the same song until loop mode is turned off. If loop mode is off, the bot will play the next song in the playlist. The command has aliases 'l' and 'repeat'. This command can only be used in a guild, not in direct messages with the bot. This command has a cooldown of 3 uses per 1 second per user. If a user tries to use the command while on cooldown, a message will be sent informing them of the remaining cooldown time."
SKIP_COMMAND_DESCRIPTION = "This command allows the user to skip the current song and play the next song in the playlist. If there are no more songs in the playlist, the command will return a message indicating that there are no more songs to play."
PREV_COMMAND_DESCRIPTION = "This command plays the previous song in the playlist of the music player. It cannot be used while in loop mode. If the music player is not connected to a voice channel, the command will not execute. If there are no previous songs in the playlist, the command will not execute."
PAUSE_COMMAND_DESCRIPTION = "The pause command allows a user to pause the audio playback of a music bot in a voice channel. If the bot is not currently playing any audio, it will send a message saying so. Otherwise, the audio will be paused and a message will be sent confirming that the audio source has been paused."
RESUME_COMMAND_DESCRIPTION = "This command resumes the audio playback in the voice channel, if it was previously paused. If the bot is not currently paused, it will return a message saying so. This command has a cooldown of 3 uses per 1 second per user, and can only be used in a server (not in direct messages)."
PLAYLIST_COMMAND_DESCRIPTION = "This command displays the current list of songs in the playlist. The bot will send a message in the text channel where the command was used, containing the name of each song, as well as its position in the playlist. If the playlist is empty, the bot will respond with a message saying that there are no songs in the playlist. Note that this command does not affect the playback of songs in the playlist."
STOP_COMMAND_DESCRIPTION = "This command will stop the currently playing audio and disconnect the bot from the voice channel. If the bot is not currently in a voice channel, it will send a message saying so. Aliases for this command are exit, quit, die, and kill."