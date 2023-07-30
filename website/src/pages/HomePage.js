import React from 'react';
import algoliasearch from 'algoliasearch/lite';
import { InstantSearch } from 'react-instantsearch-hooks';
import { Hits, RefinementList, SearchBox, Pagination } from 'react-instantsearch-hooks-web';

const searchClient = algoliasearch("0JK5MOYV7L", "cdc1ba4d5b4610337becefff57c9b2b5");

function Hit({ hit }) {
  return (
    <div className="hit-item" style={{
      display:'flex', 
      height:"330px",
      flexDirection:"column"
      }}>
      <a href={hit.product_url}>
        <b>
          <h2 style={{fontSize:"1.2rem", backgroundColor:"#F0F8FF"}}>{hit.description} </h2> 
        </b>
      </a>
      <br/>
      <div style={{position:"relative", height:"100%"}}>
        <div className='price-text' style={{position:"absolute", bottom:"172px"}}>
          <p> {hit.site} </p>
          <p style={{fontSize: "14px"}}> <b><s>{hit.original_price}</s>    Now:{hit.discounted_price}</b></p>
        </div>
        <div style={{position:"relative", height:"100%"}}>
          <a style={{bottom:"0px"}}href={hit.product_url}>
            <img 
              className='item-photo'
              style={{
                position:"absolute",
                bottom:"0px",
                height: "160px",
                width: "160px"
              }}
              src={hit.image_url}
              alt="new"
            />
          </a>
        </div>
      </div>
    </div>
  );
}

const HomePage = () => {
  return (
    <InstantSearch searchClient={searchClient} indexName="bargains">
      <SearchBox searchAsYouType={true} style={{alignSelf: "center"}}></SearchBox>

      <Pagination style={{display:"flex", alignSelf:"center"}}/>
      <div style={{ display: "flex", flexDirection: "row", paddingTop:"24px"}}>
        <div style={{ display: "flex", flexBasis: 0.33, minWidth: "300px", flexDirection:"column"}}>
          <div >
            <span style={{fontSize: "24px"}}>Origin Site</span>
            <RefinementList
              style={{paddingBottom: "20px", paddingTop: "8px", borderTop: "1px", borderStyle: "solid", borderColor:"black"}}
              attribute="site"
              limit={10}
              sortBy={["site:asc"]}
            />
          </div>
        </div>
        <div style={{ display: "flex", flexBasis: 0.67, minWidth: "900px", paddingLeft: "48px"}}>
          <Hits hitComponent={Hit} />
        </div>
      </div>
    </InstantSearch>
  );
};

export default HomePage;
