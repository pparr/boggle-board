<template>
<div v-if="gridValues">
<table 
  class="table table-bordered table-dark table-boggle">
   <tbody>
    <tr
    v-for="(row, idx) in tableRows"
    :key="row">
        <td 
        v-for="(col, idx2) in tableCols"
        :key="col">
        {{ gridValues[idx][idx2] }}
        </td>
    </tr>
  </tbody>
</table>
</div>
</template>
<script>
export default {
  name: 'BoggleGrid',
  props: { 
    tableRows: {
      type: Number,
      required: true
    },
    tableCols: {
      type: Number,
      required: true
    },
    gridValues: {
      type: Array,
      required: true
    }
  }
  }
</script>
<style>
table.table-boggle {
  text-align: center;
  width: 60%;
  height: 110%;
}
</style>