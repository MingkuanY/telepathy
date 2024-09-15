from suno import Suno, ModelVersions
client = Suno(
  cookie='A9CaGEYEOqFkKLf6CnCwGmuZuBj6f96C',
  model_version=ModelVersions.CHIRP_V3_5)

# Generate a song
songs = client.generate(prompt="A serene landscape", is_custom=False, wait_audio=True)

# Download generated songs
for song in songs:
    file_path = client.download(song=song)
    print(f"Song downloaded to: {file_path}")
    
    
