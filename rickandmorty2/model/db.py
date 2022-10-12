import sys
sys.path.append('../')
from callers import get_all_characters, get_all_episodes, get_all_locations

locations = get_all_locations()
episode_dict = get_all_episodes()
characters = get_all_characters()
