# TODO здесь писать код
gpu_old = []
total_card = int(input('Количество видеокарт: '))
for i in range(total_card):
    video_card = int(input(f'{i+1} Видеокарта: '))
    gpu_old.append(video_card)
gpu_new = []
max = gpu_old[0]
for card in gpu_old:
    if card > max:
        max = card

for i in range(total_card):
    if gpu_old[i] != max:
        gpu_new.append(gpu_old[i])

print(f'Старый список видеокарт: {gpu_old}')
print(f'новый список видеокарт: {gpu_old}')



