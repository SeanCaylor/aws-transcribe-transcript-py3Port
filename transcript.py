#!/usr/bin/env python3
from __future__ import absolute_import
from __future__ import print_function
def main():
	import sys
	import json
	import datetime
	import codecs

	filenameRaw=sys.argv[1]
	filename = filenameRaw[:-5]
	print((f"Converting file {filename}"))
	with codecs.open(filename+'.txt', 'w', 'utf-8') as w:
		with codecs.open(filenameRaw, 'r', 'utf-8') as f:
			data=json.loads(f.read())
			results = data.get("results")
			try:
				labels = data['results']['speaker_labels']['segments']
			except KeyError:
				transcript = results.get("transcripts")[0].get("transcript")
				w.write(f"{transcript}")
				return
				
			speaker_start_times={}
			for label in labels:
				for item in label['items']:
					speaker_start_times[item['start_time']] =item['speaker_label']
			items = data['results']['items']
			lines=[]
			line=''
			time=0
			speaker='null'
			i=0
			for item in items:
				i=i+1
				content = item['alternatives'][0]['content']
				if item.get('start_time'):
					current_speaker=speaker_start_times[item['start_time']]
				elif item['type'] == 'punctuation':
					line = line+content
				if current_speaker != speaker:
					if speaker:
						lines.append({'speaker':speaker, 'line':line, 'time':time})
					line=content
					speaker=current_speaker
					time=item['start_time']
				elif item['type'] != 'punctuation':
					line = line + ' ' + content
			lines.append({'speaker':speaker, 'line':line,'time':time})
			sorted_lines = sorted(lines,key=lambda k: float(k['time']))
			for line_data in sorted_lines:
				line='[' + str(datetime.timedelta(seconds=int(round(float(line_data['time']))))) + '] ' + line_data.get('speaker') + ': ' + line_data.get('line')
				w.write(line + '\n\n')


if __name__ == '__main__':
	main()
