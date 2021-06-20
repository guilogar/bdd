package hellocucumber;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

import static org.junit.Assert.*;

public class StepDefinitions {

    private Double radius;
    private Double area;
    private final Double expectedArea = 78.53981633974483;

    @Given("un radio de valor 5.0")
    public void radius_value_five() {
        this.radius = 5.0;
    }

    @When("al calcular el area")
    public void area_calc() {
        this.area = Math.PI * Math.pow(this.radius, 2);
    }

    @Then("el area es igual a 78.54")
    public void area_value_equals_to() {
        assertEquals(this.expectedArea, this.area);
    }
}
