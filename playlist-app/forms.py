"""Forms for playlist app."""

from wtforms import SelectField, StringField, TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    # Add the necessary code to use this form
    playlist_name = StringField('Playlist Name', validators=[InputRequired()])

    playlist_desc = TextAreaField('Description')


class SongForm(FlaskForm):
    """Form for adding songs."""

    # Add the necessary code to use this form
    song_title = StringField('Song Name', validators=[InputRequired()])

    song_artist = StringField('Artist', validators=[InputRequired()])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
