import {  Map, AdvancedMarker } from "@vis.gl/react-google-maps";
import { useEffect, useContext } from "react";
import { GoogleMapContext } from "../../context/GoogleMapContext";
import "./MapComponent.css";
import GoogleMapsNearByLocations from "./GoogleMapsNearByLocations";
import InfoWindowComponent from "./InfoWindowComponent";

function MapComponent() {
  const { center, newCenter, setNewCenter, nearbyStations, selectedStation, map } = useContext(GoogleMapContext);
  
  //This useEffect will run when the map and newCenter is available
    useEffect(() => {
      if (map && newCenter) {
        map.setCenter(newCenter);
      }
    }, [map, newCenter, center]);
  
    const handleDragEnd = () => {
      if (map) {
        const newCenter = map.getCenter();
        setNewCenter({ lat: newCenter.lat(), lng: newCenter.lng() });
      }
    };
  
    return (
      <Map
        onLoad={(mapInstance) =>  mapInstance.setCenter(center)}
        onDragend={handleDragEnd}
        style={{ width: '100%', height: '100vh' }}
        defaultCenter={center}
        mapId={import.meta.env.VITE_REACT_APP_GOOGLE_MAP_ID || "e2ea39204ffcffc4"}
        defaultZoom={15}
        disableDefaultUI={true}
        gestureHandling={'greedy'}
        maxZoom={20}
      >
        <AdvancedMarker position={center}>
          <div>
            <img className="user-marker" src="/user.svg" width={32} height={32} />
          </div>
        </AdvancedMarker>

        {selectedStation &&  <InfoWindowComponent /> } 
  
        <GoogleMapsNearByLocations nearbyStations={nearbyStations} />
      </Map>
    );
}
  
export default MapComponent;