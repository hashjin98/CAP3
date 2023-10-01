package cpas.model;

public class Food {
    private String storeName;  // Corresponds to store_namecol
    private String storeMenu;  // Corresponds to store_menu
    private String menuPrice;  // Corresponds to menu_price
    private String storeAddress;  // Corresponds to store_address
    private String storeTell;

    public String getStoreName() {
        return storeName;
    }

    public void setStoreName(String storeName) {
        this.storeName = storeName;
    }

    public String getStoreMenu() {
        return storeMenu;
    }

    public void setStoreMenu(String storeMenu) {
        this.storeMenu = storeMenu;
    }

    public String getMenuPrice() {
        return menuPrice;
    }

    public void setMenuPrice(String menuPrice) {
        this.menuPrice = menuPrice;
    }

    public String getStoreAddress() {
        return storeAddress;
    }

    public void setStoreAddress(String storeAddress) {
        this.storeAddress = storeAddress;
    }
    
    public String getStoreTell() {
        return storeTell;
    }

    public void setStoreTell(String storeTell) {
        this.storeTell = storeTell;
    }
}
