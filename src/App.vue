<script setup >
import { ref, onMounted} from 'vue';
import axios from 'axios';
import { Chart as ChartJS, ArcElement, Tooltip, Legend, CategoryScale, LinearScale, BarElement } from 'chart.js';
import { CalendarIcon } from '@heroicons/vue/24/outline';
import StatisticsCards from './components/StatisticsCards.vue';
import ChartSection from './components/ChartSection.vue';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'https://ada-backend-gamma.vercel.app';

// Create axios 
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json'
  }
});

ChartJS.register(ArcElement, Tooltip, Legend, CategoryScale, LinearScale, BarElement);

const totalSales = ref(0);
const trendingProducts = ref([]);
const categorySales = ref([]);
const products = ref([]);

const selectedPeriod = ref('30d');
const isLoading = ref(false);

// Cache pour stocker les données par période
const dataCache = ref({
  '7d': null,
  '30d': null,
  '12m': null
});

const fetchData = async () => {
  // Si les données sont en cache, on les utilise
  if (dataCache.value[selectedPeriod.value]) {
    const cachedData = dataCache.value[selectedPeriod.value];
    totalSales.value = cachedData.totalSales || 0;
    trendingProducts.value = cachedData.trendingProducts || [];
    categorySales.value = cachedData.categorySales || [];
    products.value = cachedData.products || [];
    return;
  }

  isLoading.value = true;
  try {
    const [totalRes, trendingRes, categoryRes, productsRes] = await Promise.all([
      api.get(`/analytics/total_sales?period=${selectedPeriod.value}`),
      api.get(`/analytics/trending_products?period=${selectedPeriod.value}`),
      api.get(`/analytics/category_sales?period=${selectedPeriod.value}`),
      api.get(`/products?period=${selectedPeriod.value}`)
    ]);

    // Mettre à jour les données avec des valeurs par défaut
    totalSales.value = totalRes.data?.totalSales || 0;
    trendingProducts.value = trendingRes.data || [];
    categorySales.value = categoryRes.data || [];
    
    products.value = (productsRes.data?.products || []).map(product => ({
      ...product,
      addDate: product.dateAdded ? new Date(product.dateAdded).toLocaleDateString('fr-FR', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit'
      }) : 'Pas de date',
      price: typeof product.price === 'number' ? product.price.toFixed(2) : '0.00',
      totalSales: product.totalSales || 0
    }));

    // Mettre en cache les données
    dataCache.value[selectedPeriod.value] = {
      totalSales: totalSales.value,
      trendingProducts: trendingProducts.value,
      categorySales: categorySales.value,
      products: products.value
    };
  } catch (error) {
    console.error('Error fetching data:', error);
    if (error.response) {
      console.error('Response error:', error.response.data);
    }
    // Reset des données en cas d'erreur
    totalSales.value = 0;
    trendingProducts.value = [];
    categorySales.value = [];
    products.value = [];
  } finally {
    isLoading.value = false;
  }
};

const updatePeriod = (period) => {
  selectedPeriod.value = period;
  fetchData();
};

onMounted(fetchData);
</script>

<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-100 to-blue-50 p-8">
    <div class="max-w-7xl mx-auto">
      <!-- Loading -->
      <div v-if="isLoading" class="fixed inset-0 bg-gray-900 bg-opacity-50 flex items-center justify-center z-50">
        <div class="bg-white p-8 rounded-lg shadow-xl flex flex-col items-center">
          <div class="animate-spin rounded-full h-16 w-16 border-t-4 border-b-4 border-blue-500 mb-4"></div>
          <p class="text-gray-700 text-lg font-semibold">Chargement des données...</p>
        </div>
      </div>

      <!-- Header -->
      <div class="flex items-center justify-between mb-8">
        <h1 class="text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-500 to-indigo-600">
          Analyse des Paniers d'Achat
        </h1>
        <div class="relative">
          <select v-model="selectedPeriod" @change="updatePeriod(selectedPeriod)" 
                  class="appearance-none bg-white border-2 border-blue-300 rounded-lg pl-4 pr-10 py-2 text-blue-600 focus:ring-2 focus:ring-blue-400 focus:border-transparent transition-all duration-200 hover:bg-blue-50">
            <option value="7d">7 derniers jours</option>
            <option value="30d">30 derniers jours</option>
            <option value="12m">12 derniers mois</option>
          </select>
          <CalendarIcon class="absolute right-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-blue-400 pointer-events-none" />
        </div>
      </div>

      <!-- Statistiques -->
      <StatisticsCards 
        :total-sales="totalSales"
        :trending-products="trendingProducts"
        :category-sales="categorySales"
      />

      <!-- Graphiques -->
      <ChartSection 
        :category-sales="categorySales"
        :products="products"
      />

      <!-- Liste des produits -->
      <div class="mt-8 bg-white rounded-lg shadow-lg overflow-hidden">
        <div class="p-6">
          <h2 class="text-2xl font-semibold text-gray-800 mb-4">Liste des Produits</h2>
          <div class="overflow-x-auto h-96">
            <table class="min-w-full divide-y divide-gray-200">
              <thead class="bg-gray-50">
                <tr>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Produit</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Date d'ajout</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Prix</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Ventes totales</th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200">
                <tr v-for="product in products" :key="product.id" class="hover:bg-gray-50">
                  <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ product.name }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ product.addDate }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ product.price }}DH</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ product.totalSales }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
