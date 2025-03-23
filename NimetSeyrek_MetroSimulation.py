import heapq
from collections import deque
import matplotlib.pyplot as plt
import networkx as nx


class Istasyon:
    def __init__(self, isim):
        self.isim = isim
        self.komsular = []

    def __str__(self):
        return self.isim

    def __repr__(self):
        return self.isim


class MetroAgi:
    def __init__(self):
        self.istasyonlar = {}

    def istasyon_ekle(self, isim):
        if isim not in self.istasyonlar:
            self.istasyonlar[isim] = Istasyon(isim)

    def baglantı_ekle(self, isim1, isim2, sure, mesafe):
        self.istasyon_ekle(isim1)
        self.istasyon_ekle(isim2)
        self.istasyonlar[isim1].komsular.append((self.istasyonlar[isim2], sure, mesafe))
        self.istasyonlar[isim2].komsular.append((self.istasyonlar[isim1], sure, mesafe))

    def en_az_aktarma_bul(self, baslangic_isim, bitis_isim):
        """
        BFS algoritmasını kullanarak en az aktarmalı rotayı bulur.
        """
        queue = deque([(baslangic_isim, [baslangic_isim])])  # (istasyon, rota)
        visited = set()

        while queue:
            istasyon, rota = queue.popleft()

            if istasyon == bitis_isim:
                return rota

            if istasyon not in visited:
                visited.add(istasyon)
                for komsu, _, _ in self.istasyonlar[istasyon].komsular:
                    if komsu.isim not in visited:
                        queue.append((komsu.isim, rota + [komsu.isim]))
        return None  # Eğer rota bulunamazsa

    def en_hizli_rota_bul(self, baslangic_isim, bitis_isim):
        """
        A* algoritmasını kullanarak en hızlı rotayı bulur.
        """

        def heuristic(istasyon1, istasyon2):
            return 0  # Bu örnekte, A*'ta heuristic sıfır alınmıştır. Gerçek dünyada mesafe kullanılır.

        open_list = []
        heapq.heappush(open_list,
                       (0, baslangic_isim, 0, [baslangic_isim]))  # (toplam maliyet, istasyon, g_degeri, rota)
        g_degerleri = {baslangic_isim: 0}
        visited = set()

        while open_list:
            _, istasyon, g_degeri, rota = heapq.heappop(open_list)

            if istasyon == bitis_isim:
                return rota

            if istasyon not in visited:
                visited.add(istasyon)
                for komsu, sure, mesafe in self.istasyonlar[istasyon].komsular:
                    if komsu.isim not in visited:
                        yeni_g_degeri = g_degeri + sure
                        if komsu.isim not in g_degerleri or yeni_g_degeri < g_degerleri[komsu.isim]:
                            g_degerleri[komsu.isim] = yeni_g_degeri
                            f_degeri = yeni_g_degeri + heuristic(komsu, self.istasyonlar[bitis_isim])
                            heapq.heappush(open_list, (f_degeri, komsu.isim, yeni_g_degeri, rota + [komsu.isim]))

        return None  # Eğer rota bulunamazsa

    def gorsellestir(self, en_az_aktarma, en_hizli_rota):
        """
        Metro ağını görselleştirir ve rotaları vurgular.
        """
        G = nx.Graph()

        # İstasyonlar ve bağlantılar
        for istasyon in self.istasyonlar.values():
            for komsu, sure, mesafe in istasyon.komsular:
                G.add_edge(istasyon.isim, komsu.isim, weight=sure)

        pos = nx.spring_layout(G)  # İstasyonların görsel yerleşimi

        plt.figure(figsize=(8, 8))
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=12, font_weight='bold',
                edge_color='gray')

        # En az aktarmalı rotayı vurgula
        if en_az_aktarma:
            route_edges = [(en_az_aktarma[i], en_az_aktarma[i + 1]) for i in range(len(en_az_aktarma) - 1)]
            nx.draw_networkx_edges(G, pos, edgelist=route_edges, edge_color='green', width=3)
            # Yolların uzunluğunu yazdır
            for i in range(len(route_edges)):
                u, v = route_edges[i]
                weight = G[u][v]['weight']
                x_pos = (pos[u][0] + pos[v][0]) / 2
                y_pos = (pos[u][1] + pos[v][1]) / 2
                plt.text(x_pos, y_pos, f"{weight}", fontsize=12, color='green', ha='center', va='center')

        # En hızlı rotayı vurgula
        if en_hizli_rota:
            route_edges = [(en_hizli_rota[i], en_hizli_rota[i + 1]) for i in range(len(en_hizli_rota) - 1)]
            nx.draw_networkx_edges(G, pos, edgelist=route_edges, edge_color='red', width=3)
            # Yolların uzunluğunu yazdır
            for i in range(len(route_edges)):
                u, v = route_edges[i]
                weight = G[u][v]['weight']
                x_pos = (pos[u][0] + pos[v][0]) / 2
                y_pos = (pos[u][1] + pos[v][1]) / 2
                plt.text(x_pos, y_pos, f"{weight}", fontsize=12, color='red', ha='center', va='center')

        plt.title("Metro Ağı ve Rotalar")
        plt.show()


# Örnek kullanım
if __name__ == "__main__":
    metro_agi = MetroAgi()

    # Metro ağını kurma (istasyonlar ve bağlantılar)
    metro_agi.baglantı_ekle('A', 'B', 2, 5)
    metro_agi.baglantı_ekle('B', 'C', 3, 10)
    metro_agi.baglantı_ekle('A', 'C', 7, 20)
    metro_agi.baglantı_ekle('C', 'D', 1, 2)
    metro_agi.baglantı_ekle('B', 'D', 5, 15)

    # Test: En az aktarmalı rota (BFS)
    en_az_aktarma = metro_agi.en_az_aktarma_bul('A', 'D')
    print("En Az Aktarmalı Rota (BFS):", en_az_aktarma)

    # Test: En hızlı rota (A*)
    en_hizli_rota = metro_agi.en_hizli_rota_bul('A', 'D')
    print("En Hızlı Rota (A*):", en_hizli_rota)

    # Görselleştirme
    metro_agi.gorsellestir(en_az_aktarma, en_hizli_rota)
