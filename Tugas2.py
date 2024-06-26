def perjalanan(graf, awal, akhir):
    stack = [(awal, [awal])]
    while stack:
        (node, path) = stack.pop()
        for next_node in graf.get(node, []):
            if next_node in path:
                continue
            if next_node == akhir:
                yield path + [next_node]
            else:
                stack.append((next_node, path + [next_node]))
def print_rute(rute):
    for i, path in enumerate(rute, start=1):
        print(f'Rute {i}: {" -> ".join(path)}')
graf_kota_china = {
    'Beijing': ['Tianjin', 'Shijiazhuang', 'Jinan'],
    'Tianjin': ['Beijing', 'Shijiazhuang'],
    'Shijiazhuang': ['Beijing', 'Tianjin', 'Zhengzhou', 'Xingtai'],
    'Jinan': ['Beijing', 'Shijiazhuang', 'Zhengzhou', 'Qingdao'],
    'Zhengzhou': ['Shijiazhuang', 'Jinan', 'Wuhan'],
    'Nanjing': ['Jinan', 'Hefei', 'Shanghai'],
    'Qingdao': ['Jinan', 'Taian'],
    'Wuhan': ['Zhengzhou', 'Changsha', 'Nanchang'],
    'Hefei': ['Nanjing', 'Wuhan'],
    'Shanghai': ['Nanjing', 'Hangzhou']
}
tempat_awal = input('Masukkan Kota Asal: ')
tempat_akhir = input('Masukkan Kota Tujuan: ')

rute = list(perjalanan(graf_kota_china, tempat_awal, tempat_akhir))
print('Jumlah Rute:', len(rute))
print()
if len(rute) > 0:
    print('Rute Tercepat:', ' -> '.join(rute[0]))
    print('Rute Terlama:', ' -> '.join(rute[-1]))
    print('\nDaftar Rute:')
    print_rute(rute)
else:
    print('Tidak ditemukan rute dari', tempat_awal, 'ke', tempat_akhir)
