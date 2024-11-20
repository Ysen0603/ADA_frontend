<script setup>
import { Pie, Bar } from 'vue-chartjs';
import { ChartPieIcon, ShoppingBagIcon } from '@heroicons/vue/24/outline';
import { computed } from 'vue';

const props = defineProps({
  categorySales: {
    type: Array,
    required: true
  },
  products: {
    type: Array,
    required: true
  }
});

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false
};

const categoryChartData = computed(() => ({
  labels: props.categorySales.map(cat => cat.category),
  datasets: [{
    data: props.categorySales.map(cat => cat.sales),
    backgroundColor: [
      '#FF6384',
      '#36A2EB',
      '#FFCE56',
      '#4BC0C0',
      '#9966FF',
      '#FF9F40'
    ]
  }]
}));

const productChartData = computed(() => ({
  labels: props.products.map(prod => prod.name),
  datasets: [{
    label: 'Ventes totales',
    data: props.products.map(prod => prod.totalSales),
    backgroundColor: '#36A2EB',
  }]
}));
</script>

<template>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
    <!-- Graphique en secteurs -->
    <div class="group bg-white bg-opacity-80 backdrop-blur-lg p-6 rounded-xl border border-blue-200 shadow-lg hover:shadow-blue-200/50 transition-all duration-300">
      <div class="flex items-center justify-between mb-4">
        <h2 class="text-xl font-semibold text-blue-600">Répartition des ventes</h2>
        <div class="p-2 bg-blue-100 rounded-lg group-hover:bg-blue-200 transition-colors duration-200">
          <ChartPieIcon class="h-6 w-6 text-blue-500" />
        </div>
      </div>
      <div class="h-80">
        <Pie v-if="categorySales.length > 0" :data="categoryChartData" :options="chartOptions" />
      </div>
    </div>

    <!-- Histogramme -->
    <div class="group bg-white bg-opacity-80 backdrop-blur-lg p-6 rounded-xl border border-indigo-200 shadow-lg hover:shadow-indigo-200/50 transition-all duration-300">
      <div class="flex items-center justify-between mb-4">
        <h2 class="text-xl font-semibold text-indigo-600">Ventes par produit</h2>
        <div class="p-2 bg-indigo-100 rounded-lg group-hover:bg-indigo-200 transition-colors duration-200">
          <ShoppingBagIcon class="h-6 w-6 text-indigo-500" />
        </div>
      </div>
      <div class="h-80">
        <Bar v-if="products.length > 0" :data="productChartData" :options="chartOptions" />
      </div>
    </div>
  </div>
</template>


