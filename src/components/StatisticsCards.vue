<script setup>
import { CurrencyEuroIcon, ArrowTrendingUpIcon, TagIcon } from '@heroicons/vue/24/outline';

defineProps({
  totalSales: {
    type: Number,
    required: true
  },
  trendingProducts: {
    type: Array,
    required: true,
    default: () => []
  },
  categorySales: {
    type: Array,
    required: true,
    default: () => []
  }
});


</script>

<template>
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
    <!-- Total des ventes -->
    <div class="group bg-white bg-opacity-80 backdrop-blur-lg p-6 rounded-xl border border-blue-200 shadow-lg hover:shadow-blue-200/50 transition-all duration-300 hover:translate-y-[-2px]">
      <div class="flex items-center justify-between mb-4">
        <h3 class="text-lg font-medium text-blue-600">Total des ventes</h3>
        <div class="p-2 bg-blue-100 rounded-lg group-hover:bg-blue-200 transition-colors duration-200">
          <CurrencyEuroIcon class="h-6 w-6 text-blue-500" />
        </div>
      </div>
      <p class="text-3xl font-bold text-gray-800">{{ (totalSales || 0).toFixed(2) }} DH</p>
    </div>

    <!-- Produits tendance -->
    <div class="group bg-white bg-opacity-80 backdrop-blur-lg p-6 rounded-xl border border-indigo-200 shadow-lg hover:shadow-indigo-200/50 transition-all duration-300 hover:translate-y-[-2px]">
      <div class="flex items-center justify-between mb-4">
        <h3 class="text-lg font-medium text-indigo-600">les 3 Produits les plus vendus</h3>
        <div class="p-2 bg-indigo-100 rounded-lg group-hover:bg-indigo-200 transition-colors duration-200">
          <ArrowTrendingUpIcon class="h-6 w-6 text-indigo-500" />
        </div>
      </div>
      <ul class="space-y-3">
        <li v-for="product in (trendingProducts || []).slice(0, 3)" :key="product._id" 
            class="flex items-center justify-between p-2 rounded-lg bg-indigo-50 hover:bg-indigo-100 transition-colors duration-200">
          <span class="text-gray-800">{{ product.name }}</span>
          <span class="text-indigo-600 font-semibold">{{ product.totalSales || 0 }}</span>
        </li>
      </ul>
    </div>

    <!-- Ventes par catégorie -->
    <div class="group bg-white bg-opacity-80 backdrop-blur-lg p-6 rounded-xl border border-sky-200 shadow-lg hover:shadow-sky-200/50 transition-all duration-300 hover:translate-y-[-2px]">
      <div class="flex items-center justify-between mb-4">
        <h3 class="text-lg font-medium text-sky-600">Répartition des ventes par catégorie</h3>
        <div class="p-2 bg-sky-100 rounded-lg group-hover:bg-sky-200 transition-colors duration-200">
          <TagIcon class="h-6 w-6 text-sky-500" />
        </div>
      </div>
      <ul class="space-y-3">
        <li v-for="category in categorySales" :key="category.category" 
            class="flex items-center justify-between p-2 rounded-lg bg-sky-50 hover:bg-sky-100 transition-colors duration-200">
          <div class="flex items-center space-x-2">
            <span class="text-gray-800">{{ category.category }}</span>
            <span class="text-gray-500 text-sm">({{ category.sales || 0 }} ventes)</span>
          </div>
          <div class="flex items-center space-x-3">
            <span class="text-sky-600 font-semibold w-16 text-right">{{ category.percentage}}%</span>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>
