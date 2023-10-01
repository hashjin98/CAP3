package cpas;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class dddd {
    private static final String JDBC_URL = "jdbc:mysql://localhost:3306/new_food_info";
    private static final String DB_USER = "root";
    private static final String DB_PASSWORD = "0000";

    public static void main(String[] args) {
        Connection connection = null;
        PreparedStatement preparedStatement = null;
        ResultSet resultSet = null;

        try {
            // Load the MySQL JDBC driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            // Get a connection to the database
            connection = DriverManager.getConnection(JDBC_URL, DB_USER, DB_PASSWORD);

            if (connection != null) {
                System.out.println("Successfully connected to the database!");

                // Define the menu name to search for
                String menuName = "asd"; // Replace with the menu name you want to search

                // Define the SQL query
                String sql = "SELECT * FROM store_han WHERE store_menu = ?";

                // Create a prepared statement
                preparedStatement = connection.prepareStatement(sql);
                preparedStatement.setString(1, menuName);

                // Execute the query
                resultSet = preparedStatement.executeQuery();

                // Process the query results
                while (resultSet.next()) {
                    String storeName = resultSet.getString("store_namecol");
                    String menu = resultSet.getString("store_menu");
                    String menuPrice = resultSet.getString("menu_price");
                    String storeAddress = resultSet.getString("store_address");

                    // Print the menu information to the console
                    System.out.println("Store Name: " + storeName);
                    System.out.println("Menu: " + menu);
                    System.out.println("Menu Price: " + menuPrice);
                    System.out.println("Store Address: " + storeAddress);
                    System.out.println("-------------");
                }
            } else {
                System.out.println("Failed to connect to the database.");
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.out.println("Connection failed due to: " + e.getMessage());
        } finally {
            try {
                if (resultSet != null) {
                    resultSet.close();
                }
                if (preparedStatement != null) {
                    preparedStatement.close();
                }
                if (connection != null) {
                    connection.close();
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}