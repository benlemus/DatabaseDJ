from flask import Flask, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError, OperationalError

from models import db, connect_db, Playlist, Song, PlaylistSong
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

app.debug = True

connect_db(app)
with app.app_context():
    db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.route("/")
def root():
    """Homepage: redirect to /playlists."""

    return redirect("/playlists")


##############################################################################
# Playlist routes


@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""

    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)


@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

    playlist = Playlist.query.filter_by(id=playlist_id).first()

    songs = playlist.songs.all()

    if not playlist:
        flash(f'Could Not Get Playlist, "playlist id": {playlist_id}', category='danger')
        return redirect('/playlists')
    
    return render_template('playlist.html', playlist=playlist, songs=songs)


@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

    form = PlaylistForm()

    if form.validate_on_submit():
        name = form.playlist_name.data
        desc = form.playlist_desc.data
     
        new_playlist = Playlist(name=name, description=desc)

        try:
            db.session.add(new_playlist)
            db.session.commit()
            
            flash(f'Playlist "{new_playlist.name}" Added!', category='success')
            return redirect('/playlists')
        
        except IntegrityError:
            db.session.rollback()
            flash('Playlist Name Already Exists', category='danger')
            return redirect('/playlists/add')

        except OperationalError:
            db.session.rollback()
            flash('Database Error', category='danger')
            return redirect('/playlists/add')
        
        except Exception as e:
            db.session.rollback()
            flash(f'Could Not Add Playlist', category='danger')
            return redirect('/playlists/add')
        
    return render_template('new_playlist.html', form=form)


##############################################################################
# Song routes


@app.route("/songs")
def show_all_songs():
    """Show list of songs."""

    songs = Song.query.all()
    return render_template("songs.html", songs=songs)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

    song = Song.query.filter_by(id=song_id).first()

    playlists = song.playlists

    if not song:
        flash(f'Could Not Get Song, "song id": {song_id}', category='danger')
        return redirect('/songs')

    return render_template('song.html', song=song, playlists=playlists)

@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

    form = SongForm()

    if form.validate_on_submit():
        title = form.song_title.data
        artist = form.song_artist.data

        new_song = Song(title=title, artist=artist)

        try:
            db.session.add(new_song)
            db.session.commit()

            flash(f'Song "{new_song.title}" Added!', category='success')
            return redirect('/songs')

        except IntegrityError:
            db.session.rollback()
            flash('Playlist Name Already Exists', category='danger')
            return redirect('/songs/add')

        except OperationalError:
            db.session.rollback()
            flash('Database Error', category='danger')
            return redirect('/songs/add')
        
        except Exception as e:
            db.session.rollback()
            flash(f'Could Not Add Playlist', category='danger')
            return redirect('/songs/add')
        
    return render_template('new_song.html', form=form)

@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""

    # BONUS - ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

    # THE SOLUTION TO THIS IS IN A HINT IN THE ASSESSMENT INSTRUCTIONS

    playlist = Playlist.query.get_or_404(playlist_id)
    form = NewSongForPlaylistForm()

    # Restrict form to songs not already on this playlist

    curr_on_playlist = [song.id for song in playlist.songs]

    form.song.choices = [(song.id, song.title) for song in db.session.query(Song).filter(Song.id.notin_(curr_on_playlist)).all()]

    if form.validate_on_submit():

          # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
        try:
            playlist_song = PlaylistSong(song_id=form.song.data, playlist_id=playlist_id)
            db.session.add(playlist_song)
            db.session.commit()

            flash(f'Song Added To Playlist!', category='success')
            return redirect(f"/playlists/{playlist_id}")

        except OperationalError:
            db.session.rollback()
            flash('Database Error', category='danger')
            return redirect(f'/playlists/{playlist_id}/add-song')
        
        except Exception as e:
            db.session.rollback()
            flash(f'Could Not Add Playlist', category='danger')
            return redirect(f'/playlists/{playlist_id}/add-song')
        
    return render_template("add_song_to_playlist.html", playlist=playlist, form=form)
