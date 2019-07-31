<template>
  <div>
    <b-container fluid>
      <b-row>
        <b-col md="2" offset="8">
        <label for="gridSelect">Grid Size</label>
      <b-form-select
        class="gridSelect mb-1" 
        v-model="selected" 
        :options="options"
        @change="setGridSize">
      </b-form-select>
        </b-col>
      </b-row>
    <b-row>
      <b-col align="center">
   <bogglegrid
   :grid-values="this.gridVals"
   :table-rows="this.tableRows"
   :table-cols="this.tableCols" />
      </b-col>
    </b-row>
    <b-row>
      <b-col align="center" class="ml-1 mb-2">
        <button type="button" 
            class="btn btn-primary"
            @click="getGridValues">
            New Board
            </button>
        <!-- disabling because not implemented-->
        <button type="button" 
            class="btn btn-primary m-1"
            @click="solveBoard"
            :disabled="true">
            Solve Board
            </button>
      </b-col>
    </b-row>
    <b-row>
      <b-col align="center">
        <label for="solutionbox">Solutions</label>
        <solutionbox class="solutionbox"
        :solution-list="this.solutions"/>
      </b-col>
    </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios';
import bogglegrid from '@/components/BoggleGrid';
import solutionbox from '@/components/SolutionBox';

export default {
  name: 'Board',
  components: {
    bogglegrid, 
    solutionbox
  },
  data() {
    return {
      gridSize: 16, 
      tableRows: 4,
      tableCols: 4,
      gridVals: Array(this.gridSize).fill(''),
      solutions: [],
      selected: '4x4',
      options: [
          { value: '4x4', text: '4x4' },
          { value: '5x5', text: '5x5' },
          { value: '6x6', text: '6x6' }
      ]
    };
  },

  methods: {
    getGridValues() {
      const path = 'http://localhost:5000/letters';
      axios.get(path)
        .then((res) => {
          this.gridVals = res.data;
          console.log(this.gridVals);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    setGridSize() {
      const path = 'http://localhost:5000/gridsize';
      axios.post(path, 
      {
        data: {
        selected: this.selected }
      })
      .then(res => {
      console.log(res.data)
      this.tableRows = parseInt(res.data)
      this.tableCols = parseInt(res.data)
      this.gridSize = this.tableRows * this.tableCols
      })
      .catch(error => {
      console.log(error)
    });
    },
    // TODO-not implemented, returns dummy strings
    solveBoard() {
      const path = 'http://localhost:5000/solve';
       axios.get(path)
        .then((res) => {
          this.solutions = res.data;
          console.log(this.solutions);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    }
  },
  created() {
    this.setGridSize();
    this.getGridValues();
    this.solveBoard();
    
  },
};
</script>
<style>

</style>