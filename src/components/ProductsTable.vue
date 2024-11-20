
<script setup>
import { ShoppingBagIcon } from '@heroicons/vue/24/outline';

defineProps({
  products: {
    type: Array,
    required: true
  },
  isLoading: {
    type: Boolean,
    required: true
  }
});
</script>

<template>
  <div class="bg-white bg-opacity-80 backdrop-blur-lg rounded-xl border border-blue-200 shadow-lg overflow-hidden transition-all duration-300">
    <div class="p-6 border-b border-blue-200 flex justify-between items-center">
      <div class="flex items-center space-x-3">
        <ShoppingBagIcon class="h-6 w-6 text-blue-500" />
        <h2 class="text-xl font-semibold text-blue-600">Liste des produits</h2>
      </div>
      <div v-if="isLoading" class="flex items-center space-x-2 text-blue-500">
        <svg class="animate-spin h-5 w-5" fill="none" viewBox="0 0 24 24">
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
          <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
        </svg>
        <span>Chargement...</span>
      </div>
    </div>

    <div class="overflow-x-auto">
      <table class="min-w-full divide-y divide-blue-200 products-table">
        <thead class="bg-blue-50">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium text-blue-500 uppercase tracking-wider">Produit</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-blue-500 uppercase tracking-wider">Prix</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-blue-500 uppercase tracking-wider">Date d'ajout</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-blue-500 uppercase tracking-wider">Ventes totales</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-blue-200">
          <tr v-for="product in products" :key="product._id" class="hover:bg-blue-50 transition-colors duration-200">
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm font-medium text-gray-900">{{ product.name }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm text-gray-900">{{ product.price }} DH</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm text-gray-900">{{ product.addDate }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm text-gray-900">{{ product.totalSales }}</div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

